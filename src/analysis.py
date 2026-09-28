"""
analysis.py
===========
Analisis ekonomi Indonesia dari data World Bank (1960–2025).

Struktur:
- load()                : muat data wide + long
- era_summary()         : ringkasan per era ekonomi (Orde Baru / Krisis / Reformasi / Modern)
- cagr()                : pertumbuhan majemuk antar periode
- correlation_matrix()  : korelasi antar indikator (Pearson & Spearman manual)
- crisis_impact()       : dampak krisis 1998 & 2020 pada tiap indikator
- key_insights()        : temuan utama siap dilaporkan
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "data" / "processed"
RAW = ROOT / "data" / "raw"

# Era ekonomi Indonesia (periode kunci)
ERAS = [
    ("1960–1966", 1960, 1966, "Orde Lama / akhir"),
    ("1967–1997", 1967, 1997, "Orde Baru (boom)"),
    ("1998–1999", 1998, 1999, "Krisis Asia"),
    ("2000–2013", 2000, 2013, "Reformasi & boom komoditas"),
    ("2014–2019", 2014, 2019, "Perlambatan"),
    ("2020–2021", 2020, 2021, "COVID-19"),
    ("2022–2025", 2022, 2025, "Pemulihan pasca-COVID"),
]


def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    wide = pd.read_csv(PROC / "indonesia_indicators_wide.csv", index_col="year")
    long = pd.read_csv(RAW / "indonesia_indicators_long.csv")
    return wide, long


def era_summary(wide: pd.DataFrame, indicator: str) -> pd.DataFrame:
    """Rata-rata indikator per era ekonomi."""
    s = wide[indicator].dropna()
    rows = []
    for name, y0, y1, label in ERAS:
        seg = s[(s.index >= y0) & (s.index <= y1)]
        if len(seg):
            rows.append({
                "era": name, "label": label, "years": len(seg),
                "mean": round(seg.mean(), 2),
                "min": round(seg.min(), 2), "max": round(seg.max(), 2),
            })
    return pd.DataFrame(rows)


def cagr(series: pd.Series, y0: int, y1: int) -> float | None:
    """Compound annual growth rate antar dua tahun (%)."""
    try:
        a, b = series.loc[y0], series.loc[y1]
        n = y1 - y0
        if a and a > 0 and b and b > 0 and n > 0:
            return round(((b / a) ** (1 / n) - 1) * 100, 2)
    except KeyError:
        pass
    return None


def rank_correlation(a: pd.Series, b: pd.Series) -> float:
    """Spearman tanpa scipy (Pearson dari rank)."""
    df = pd.concat([a, b], axis=1).dropna()
    if len(df) < 3:
        return float("nan")
    return float(df.iloc[:, 0].rank().corr(df.iloc[:, 1].rank()))


def correlation_matrix(wide: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    cols = [c for c in wide.columns if wide[c].notna().sum() >= 20]
    if method == "pearson":
        return wide[cols].corr().round(2)
    # spearman manual
    m = pd.DataFrame(index=cols, columns=cols, dtype=float)
    for i in cols:
        for j in cols:
            m.loc[i, j] = rank_correlation(wide[i], wide[j])
    return m.astype(float).round(2)


def crisis_impact(wide: pd.DataFrame) -> pd.DataFrame:
    """Bandingkan nilai indikator sebelum vs saat krisis 1998 & 2020."""
    metrics = ["gdp_growth_pct", "inflation_pct", "unemployment_pct",
               "gdp_usd", "gini"]
    rows = []
    for ind in metrics:
        if ind not in wide.columns:
            continue
        s = wide[ind]
        def v(year):
            return round(s.loc[year], 2) if year in s.index and pd.notna(s.loc[year]) else None
        rows.append({
            "indicator": ind,
            "pre_1997": v(1997), "crisis_1998": v(1998), "recovery_2000": v(2000),
            "pre_2019": v(2019), "covid_2020": v(2020), "post_2022": v(2022),
        })
    return pd.DataFrame(rows)


def latest(wide: pd.DataFrame, indicator: str, n: int = 5) -> pd.Series:
    """n nilai terakhir yang tersedia untuk indikator."""
    return wide[indicator].dropna().tail(n)


def key_insights(wide: pd.DataFrame) -> dict:
    """Hitung insight kunci untuk laporan."""
    s = wide
    out = {}

    # GDP per kapita
    if "gdp_per_capita_usd" in s:
        pc = s["gdp_per_capita_usd"]
        out["gdp_pc_1967"] = round(pc.loc[1967], 0) if 1967 in pc.index else None
        out["gdp_pc_latest"] = round(pc.dropna().iloc[-1], 0)
        out["gdp_pc_latest_year"] = int(pc.dropna().index[-1])
        out["gdp_pc_cagr_1967_2025"] = cagr(pc, 1967, min(2025, pc.dropna().index[-1]))

    # Populasi
    if "population" in s:
        pop = s["population"].dropna()
        out["pop_1960"] = int(pop.loc[1960]) if 1960 in pop.index else None
        out["pop_latest"] = int(pop.iloc[-1])
        out["pop_latest_year"] = int(pop.index[-1])

    # Inflasi ekstrem
    if "inflation_pct" in s:
        inf = s["inflation_pct"].dropna()
        out["inflation_max"] = round(inf.max(), 1)
        out["inflation_max_year"] = int(inf.idxmax())
        out["inflation_latest"] = round(inf.iloc[-1], 1)
        out["inflation_latest_year"] = int(inf.index[-1])

    # GDP growth
    if "gdp_growth_pct" in s:
        g = s["gdp_growth_pct"].dropna()
        out["growth_min"] = round(g.min(), 1)
        out["growth_min_year"] = int(g.idxmin())
        out["growth_latest"] = round(g.iloc[-1], 1)

    # Urbanisasi
    if "urban_pct" in s:
        u = s["urban_pct"].dropna()
        out["urban_1960"] = round(u.loc[1960], 1) if 1960 in u.index else None
        out["urban_latest"] = round(u.iloc[-1], 1)

    # Internet
    if "internet_pct" in s:
        i = s["internet_pct"].dropna()
        out["internet_2000"] = round(i.loc[2000], 1) if 2000 in i.index else None
        out["internet_latest"] = round(i.iloc[-1], 1)

    # Harapan hidup
    if "life_expectancy" in s:
        le = s["life_expectancy"].dropna()
        out["life_1960"] = round(le.loc[1960], 1) if 1960 in le.index else None
        out["life_latest"] = round(le.iloc[-1], 1)

    return out


if __name__ == "__main__":
    wide, long = load()
    print("=" * 68)
    print("INDONESIA ECONOMIC INTELLIGENCE — SNAPSHOT")
    print("=" * 68)
    print(f"\nPeriode data : {wide.index.min()}–{wide.index.max()} "
          f"({wide.shape[0]} tahun, {wide.shape[1]} indikator)")

    ins = key_insights(wide)
    print("\n[Insight Utama]")
    for k, v in ins.items():
        print(f"  {k:<28}: {v}")

    print("\n[Era: GDP per kapita rata-rata (US$)]")
    print(era_summary(wide, "gdp_per_capita_usd").to_string(index=False))

    print("\n[Dampak Krisis]")
    print(crisis_impact(wide).to_string(index=False))
