"""
run_analysis.py
===============
Orkestrator: jalankan seluruh analisis & simpan tabel + ringkasan.

Output -> reports/tables/*.csv, reports/summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

import analysis as A
import forecast as F

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "reports" / "tables"
TABLES.mkdir(parents=True, exist_ok=True)


def main():
    wide, long = A.load()
    summary = {"years": [int(wide.index.min()), int(wide.index.max())],
               "n_indicators": int(wide.shape[1])}

    # ---- tabel: ringkasan era untuk indikator kunci ----
    for ind in ["gdp_per_capita_usd", "inflation_pct", "population",
                "urban_pct", "life_expectancy", "internet_pct"]:
        t = A.era_summary(wide, ind)
        t.to_csv(TABLES / f"era_{ind}.csv", index=False)
    print(f"[tables] era summaries: 6")

    # ---- dampak krisis ----
    t = A.crisis_impact(wide)
    t.to_csv(TABLES / "crisis_impact.csv", index=False)
    print(f"[tables] crisis_impact.csv ({len(t)})")

    # ---- korelasi ----
    corr = A.correlation_matrix(wide, "pearson")
    corr.to_csv(TABLES / "correlation_pearson.csv")
    corr_sp = A.correlation_matrix(wide, "spearman")
    corr_sp.to_csv(TABLES / "correlation_spearman.csv")
    print(f"[tables] correlation matrices ({corr.shape})")

    # ---- forecast ----
    fc = F.forecast_all(wide, horizon=5)
    ft = F.summary_table(fc, 5)
    ft.to_csv(TABLES / "forecast_summary.csv", index=False)
    print(f"[tables] forecast_summary.csv ({len(ft)})")

    # simpan deret forecast
    rows = []
    for ind, r in fc.items():
        for y, v in r["forecast"].items():
            rows.append({"indicator": ind, "year": y, "value": v})
    if rows:
        pd.DataFrame(rows).to_csv(TABLES / "forecast_series.csv", index=False)

    # ---- insight kunci ----
    ins = A.key_insights(wide)
    summary["insights"] = ins
    summary["forecast"] = ft.to_dict(orient="records")

    (ROOT / "reports" / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[json] summary.json")

    # simpan wide & long juga ke processed (untuk dashboard)
    wide.to_csv(ROOT / "data" / "processed" / "indicators_wide.csv")
    print("\n=== INSIGHT KUNCI ===")
    for k, v in ins.items():
        print(f"  {k:<26}: {v}")


if __name__ == "__main__":
    main()
