"""
make_charts.py
==============
Visualisasi analisis ekonomi Indonesia -> reports/figures/*.png
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import analysis as A
import forecast as F

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "reports" / "figures"
PROC = ROOT / "data" / "processed"
FIG.mkdir(parents=True, exist_ok=True)

# Palet (nuansa merah-putih Indonesia + hijau)
C = {
    "primary": "#C0392B",   # merah
    "accent": "#E4A11B",    # kuning
    "dark": "#1B2A33",
    "grey": "#8B9AA6",
    "green": "#1F5C3D",
    "blue": "#2E6F95",
}
SERIES = [C["primary"], C["blue"], C["green"], C["accent"], "#6A4C93", "#2A9D8F"]

plt.rcParams.update({
    "figure.dpi": 130, "savefig.dpi": 130, "font.size": 10,
    "axes.titlesize": 12, "axes.titleweight": "bold",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": "#CCCCCC", "axes.grid": True,
    "grid.color": "#EEEEEE", "grid.linewidth": 0.8, "figure.facecolor": "white",
})


def _save(fig, name):
    fp = FIG / f"{name}.png"
    fig.tight_layout()
    fig.savefig(fp, bbox_inches="tight")
    plt.close(fig)
    print(f"  [fig] {fp.name}")


def _shade_eras(ax, wide):
    """Beri bayangan periode krisis untuk konteks."""
    for y0, y1, col in [(1998, 1999, "#F4CCCC"), (2020, 2021, "#D9EAD3")]:
        if y1 >= wide.index.min():
            ax.axvspan(y0, y1, color=col, alpha=0.5, zorder=0)


# 1. GDP per kapita jangka panjang (1967–2025)
def chart_gdp_pc(wide):
    fig, ax = plt.subplots(figsize=(10, 5))
    s = wide["gdp_per_capita_usd"].dropna()
    ax.plot(s.index, s.values, color=C["primary"], lw=2.2, zorder=3)
    ax.fill_between(s.index, s.values, color=C["primary"], alpha=0.12)
    _shade_eras(ax, wide)
    ax.set_title("GDP per Capita Indonesia, 1967–2025\n(shaded: Asian Crisis 1998, COVID-19 2020)")
    ax.set_ylabel("US$ (current)")
    ax.yaxis.set_major_formatter(lambda x, p: f"${x:,.0f}")
    for y in (1967, 1997, 1998, 2025):
        if y in s.index:
            ax.annotate(f"{y}\n${s.loc[y]:,.0f}", (y, s.loc[y]),
                        fontsize=7.5, ha="center", va="bottom", color=C["dark"])
    _save(fig, "01_gdp_per_capita")


# 2. Pertumbuhan GDP + inflasi (dual)
def chart_growth_inflation(wide):
    fig, ax = plt.subplots(figsize=(10, 5))
    g = wide["gdp_growth_pct"].dropna()
    ax.bar(g.index, g.values, color=C["green"], label="GDP growth (%)", zorder=3)
    ax.axhline(0, color=C["dark"], lw=0.8)
    _shade_eras(ax, wide)
    ax.set_title("GDP Growth Indonesia, 1961–2025")
    ax.set_ylabel("% annual")
    ax.annotate(f"{int(g.idxmin())}: {g.min():.1f}%",
                (g.idxmin(), g.min()), fontsize=8, color=C["primary"],
                ha="left", va="top")
    _save(fig, "02_gdp_growth")

    # inflasi (log scale krn puncak 1136%)
    fig, ax = plt.subplots(figsize=(10, 5))
    inf = wide["inflation_pct"].dropna()
    inf = inf[inf > 0]
    ax.plot(inf.index, inf.values, color=C["accent"], lw=2, zorder=3)
    ax.set_yscale("log")
    _shade_eras(ax, wide)
    ax.set_title("Inflation Indonesia, 1960–2025 (log scale)\n"
                 f"Peak {inf.max():,.0f}% in {int(inf.idxmax())} during hyperinflation")
    ax.set_ylabel("% (log)")
    _save(fig, "03_inflation")


# 3. Populasi & urbanisasi (dual)
def chart_pop_urban(wide):
    fig, ax = plt.subplots(figsize=(10, 5))
    pop = wide["population"].dropna() / 1e6
    ax.plot(pop.index, pop.values, color=C["blue"], lw=2.2, label="Population (millions)")
    ax.set_ylabel("Population (million)", color=C["blue"])
    ax.tick_params(axis="y", labelcolor=C["blue"])
    ax2 = ax.twinx()
    urb = wide["urban_pct"].dropna()
    ax2.plot(urb.index, urb.values, color=C["green"], lw=2, ls="--", label="Urban (%)")
    ax2.set_ylabel("Urban population (%)", color=C["green"])
    ax2.tick_params(axis="y", labelcolor=C["green"])
    ax2.grid(False)
    ax.set_title("Population Growth & Urbanisation, 1960–2025")
    _save(fig, "04_population_urban")


# 4. Harapan hidup & internet (indikator sosial)
def chart_social(wide):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    le = wide["life_expectancy"].dropna()
    axes[0].plot(le.index, le.values, color=C["green"], lw=2.2)
    axes[0].set_title("Life Expectancy (years)")
    axes[0].set_ylabel("years")
    for y in (1960, 2024):
        if y in le.index:
            axes[0].annotate(f"{le.loc[y]:.1f}", (y, le.loc[y]), fontsize=8)

    net = wide["internet_pct"].dropna()
    axes[1].plot(net.index, net.values, color=C["blue"], lw=2.2)
    axes[1].set_title("Internet Users (% of population)")
    axes[1].set_ylabel("%")
    for y in (net.index.min(), net.index.max()):
        axes[1].annotate(f"{net.loc[y]:.1f}%", (y, net.loc[y]), fontsize=8)
    fig.suptitle("Social Progress Indicators", fontsize=13, fontweight="bold")
    _save(fig, "05_social_indicators")


# 5. Korelasi heatmap
def chart_correlation(wide):
    corr = A.correlation_matrix(wide, "pearson")
    # pilih subset indikator yang bermakna
    keys = ["gdp_per_capita_usd", "gdp_growth_pct", "inflation_pct", "population",
            "urban_pct", "life_expectancy", "internet_pct", "unemployment_pct",
            "exports_pct_gdp", "co2_mt"]
    keys = [k for k in keys if k in corr.columns]
    sub = corr.loc[keys, keys]
    fig, ax = plt.subplots(figsize=(9, 7.5))
    im = ax.imshow(sub.values, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(keys)))
    ax.set_yticks(range(len(keys)))
    ax.set_xticklabels([k.replace("_", " ")[:12] for k in keys], rotation=45,
                       ha="right", fontsize=7.5)
    ax.set_yticklabels([k.replace("_", " ")[:16] for k in keys], fontsize=7.5)
    for i in range(len(keys)):
        for j in range(len(keys)):
            v = sub.values[i, j]
            if not np.isnan(v):
                ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                        fontsize=6.5, color="white" if abs(v) > 0.5 else C["dark"])
    fig.colorbar(im, ax=ax, shrink=0.8, label="Pearson r")
    ax.set_title("Correlation Between Indonesian Economic Indicators (1960–2025)")
    ax.grid(False)
    _save(fig, "06_correlation")


# 6. Forecast GDP per kapita
def chart_forecast(wide):
    fc = F.forecast_all(wide, horizon=5)
    r = fc["gdp_per_capita_usd"]
    fig, ax = plt.subplots(figsize=(10, 5))
    h = r["history"]
    f = r["forecast"]
    ax.plot(h.index, h.values, color=C["dark"], lw=2.2, label="Actual")
    ax.plot([h.index[-1]] + list(f.index), [h.iloc[-1]] + list(f.values),
            color=C["primary"], lw=2.2, ls="--", marker="o", ms=4,
            label="Forecast")
    fv = np.asarray(f.values, dtype=float)
    ax.fill_between(list(f.index), fv * 0.95, fv * 1.05,
                    color=C["primary"], alpha=0.15, label="±5% band")
    ax.axvline(h.index[-1], color=C["grey"], ls=":", lw=1)
    ax.set_title(f"GDP per Capita Forecast to {int(f.index[-1])}\n"
                 f"(R²={r['r2']}, backtest MAPE={r['mape_pct']}%)")
    ax.set_ylabel("US$")
    ax.yaxis.set_major_formatter(lambda x, p: f"${x:,.0f}")
    ax.legend(loc="upper left", frameon=False)
    _save(fig, "07_forecast_gdp_pc")


# 7. Era comparison (bar)
def chart_eras(wide):
    t = A.era_summary(wide, "gdp_per_capita_usd")
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(t["era"], t["mean"], color=C["primary"], zorder=3)
    for b, m, lo, hi in zip(bars, t["mean"], t["min"], t["max"]):
        ax.text(m + 40, b.get_y() + b.get_height() / 2,
                f"${m:,.0f}  (range ${lo:,.0f}–${hi:,.0f})",
                va="center", fontsize=8, color=C["dark"])
    ax.set_xlim(0, t["mean"].max() * 1.6)
    ax.set_title("Average GDP per Capita by Economic Era")
    ax.set_xlabel("US$ (average of era)")
    ax.grid(axis="y", visible=False)
    _save(fig, "08_eras")


def build_all():
    wide, _ = A.load()
    print("Membuat visualisasi...")
    chart_gdp_pc(wide)
    chart_growth_inflation(wide)
    chart_pop_urban(wide)
    chart_social(wide)
    chart_correlation(wide)
    chart_forecast(wide)
    chart_eras(wide)
    print(f"\n[OK] gambar di {FIG}")


if __name__ == "__main__":
    build_all()
