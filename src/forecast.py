"""
forecast.py
===========
Peramalan indikator ekonomi Indonesia untuk beberapa tahun ke depan.

Pendekatan (TANPA library eksternal berat, agar ringan & reproducible):
- **Log-linear trend** untuk indikator yang tumbuh eksponensial (GDP, populasi,
  GDP per kapita) -> regresi linear pada log(nilai).
- **Linear trend + dampak** untuk indikator yang lebih stabil (inflasi, harapan
  hidup, urbanisasi, internet).
- Metrik kualitas: R², MAPE (mean absolute percentage error) via backtest
  walk-forward sederhana.

Semua fungsi mengembalikan DataFrame agar mudah dipakai report/dashboard.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "data" / "processed"

# indikator: (mode, tahun_awal_analisis)
#  'log'      = tren eksponensial (regresi pada log)
#  'linear'   = tren linear
#  'damped'   = tren linear yang diredam (untuk kurva-S seperti internet)
#  'mean_rev' = kembali ke rata-rata jangka panjang (untuk inflasi yang volatil)
#
# PENTING (pelajaran dari uji coba): memakai SELURUH sejarah (mis. 1967–2025)
# untuk meramal GDP menghasilkan angka tak realistis (+117% / 5 tahun) karena
# memasukkan era pertumbuhan tinggi yang sudah berakhir. Untuk proyeksi,
# pakai REZIM TERKINI (15 tahun terakhir) yang lebih relevan.
FORECAST_TARGETS = {
    "gdp_usd":            ("log",    2010),
    "gdp_per_capita_usd": ("log",    2010),
    "population":         ("log",    1990),
    "urban_pct":          ("linear", 1990),
    "life_expectancy":    ("linear", 1980),
    "internet_pct":       ("damped", 2005),
    "inflation_pct":      ("mean_rev", 2005),
    "co2_mt":             ("log",    2000),
}


def _fit(x: np.ndarray, y: np.ndarray, mode: str):
    """Kembalikan (slope, intercept, mode_efektif) sesuai jenis model."""
    if mode == "log":
        yt = np.log(y)
        slope, intercept = np.polyfit(x, yt, 1)
        return slope, intercept, "log"
    # linear / damped / mean_rev semuanya pakai tren linear dasar
    xs = x - x.mean()  # pusatkan agar intercept stabil
    slope, intercept = np.polyfit(xs, y, 1)
    return slope, intercept, mode


def _predict(slope, intercept, x, mode, x_ref=None):
    if mode == "log":
        return np.exp(slope * x + intercept)
    xs = x - (x_ref if x_ref is not None else 0)
    return slope * xs + intercept


def _predict_path(hist_years, hist_vals, slope, intercept, mode, fut_years,
                  horizon):
    """Hitung prediksi untuk mode 'log', 'linear', 'damped', 'mean_rev'."""
    x_ref = hist_years.mean()
    if mode in ("linear",):
        return slope * (fut_years - x_ref) + intercept
    if mode == "damped":
        # redam tren: tiap tahun tambahan dikali faktor (phi) menurun
        phi = 0.85
        base = slope * (hist_years[-1] - x_ref) + intercept
        out, step = [], 0.0
        phi_sum = 1.0
        for k in range(1, horizon + 1):
            step += slope * (phi ** k)
            out.append(base + step)
        return np.array(out)
    if mode == "mean_rev":
        # kembali perlahan ke rata-rata 10 tahun terakhir
        recent = hist_vals[-10:]
        long_mean = float(np.mean(recent))
        last = float(hist_vals[-1])
        out, val = [], last
        for k in range(1, horizon + 1):
            val = val + 0.5 * (long_mean - val)
            out.append(val)
        return np.array(out)
    # fallback linear
    return slope * (fut_years - x_ref) + intercept


def _backtest(x, y, mode, horizon=5):
    """Walk-forward: latih s/d n-horizon, prediksi horizon, hitung MAPE."""
    errs = []
    for split in range(max(10, len(x) - horizon), len(x)):
        sl, ic, md = _fit(x[:split], y[:split], mode)
        if md == "log":
            pred = _predict(sl, ic, np.array([x[split]]), md)[0]
        else:
            pred = _predict_path(x[:split], y[:split], sl, ic, md,
                                 np.array([x[split]]), 1)[0]
        if y[split] and y[split] != 0:
            errs.append(abs((pred - y[split]) / y[split]) * 100)
    return round(float(np.mean(errs)), 2) if errs else None


def forecast_series(wide: pd.DataFrame, indicator: str, mode: str,
                    y0: int, horizon: int = 5) -> dict:
    s = wide[indicator].dropna()
    s = s[s.index >= y0]
    if len(s) < 5:
        return {}
    x = s.index.values.astype(float)
    y = s.values.astype(float)
    slope, intercept, md = _fit(x, y, mode)

    # R²
    if md == "log":
        fit = np.exp(slope * x + intercept)
    else:
        fit = slope * (x - x.mean()) + intercept
    ss_res = np.sum((y - fit) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = round(1 - ss_res / ss_tot, 4) if ss_tot else None

    last_year = int(x[-1])
    fut_years = np.arange(last_year + 1, last_year + 1 + horizon, dtype=float)
    if md == "log":
        fut_vals = np.exp(slope * fut_years + intercept)
    else:
        fut_vals = _predict_path(x, y, slope, intercept, md, fut_years, horizon)

    return {
        "indicator": indicator,
        "mode": md,
        "r2": r2,
        "mape_pct": _backtest(x, y, mode),
        "history": pd.Series(y, index=s.index.astype(int)),
        "forecast": pd.Series(np.round(fut_vals, 2),
                              index=fut_years.astype(int)),
    }


def forecast_all(wide: pd.DataFrame, horizon: int = 5) -> dict:
    out = {}
    for ind, (mode, y0) in FORECAST_TARGETS.items():
        if ind in wide.columns:
            res = forecast_series(wide, ind, mode, y0, horizon)
            if res:
                out[ind] = res
    return out


def summary_table(forecasts: dict, horizon: int = 5) -> pd.DataFrame:
    """Ringkasan: nilai terakhir vs prediksi beberapa tahun, + kualitas model."""
    rows = []
    for ind, r in forecasts.items():
        hist = r["history"]
        fc = r["forecast"]
        last_year = int(hist.index[-1])
        last_val = float(hist.iloc[-1])
        rows.append({
            "indicator": ind,
            "method": r["mode"],
            "r2": r["r2"],
            "mape_pct": r["mape_pct"],
            "last_year": last_year,
            "last_value": round(last_val, 2),
            f"pred_{last_year + horizon}": round(float(fc.iloc[-1]), 2),
            "growth_pct": round((float(fc.iloc[-1]) / last_val - 1) * 100, 1)
            if last_val else None,
        })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    wide = pd.read_csv(PROC / "indonesia_indicators_wide.csv", index_col="year")
    fc = forecast_all(wide, horizon=5)
    print("=" * 70)
    print("FORECAST — INDONESIA (horizon 5 tahun)")
    print("=" * 70)
    print(summary_table(fc, 5).to_string(index=False))
    print("\nContoh deret GDP per kapita:")
    r = fc.get("gdp_per_capita_usd", {})
    for y, v in r.get("forecast", {}).items():
        print(f"  {y}: US$ {v:,.0f}")
