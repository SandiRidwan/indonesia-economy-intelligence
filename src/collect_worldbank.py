"""
collect_worldbank.py
====================
Mengumpulkan 17 indikator ekonomi Indonesia dari World Bank API (1960–2025).

Sumber: https://api.worldbank.org (World Bank Open Data, publik & gratis)

Design:
- Definisikan indikator + metadata ramah-manusia (nama pendek, unit, kategori).
- Ambil per indikator (pagination), simpan mentah ke data/raw/.
- Simpan juga versi "long" (Country, Indicator, Year, Value) & "wide"
  (Year x Indicator) untuk analisis.

Jalankan: python src/collect_worldbank.py
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
RAW.mkdir(parents=True, exist_ok=True)
PROC.mkdir(parents=True, exist_ok=True)

COUNTRY = "IDN"          # Indonesia
ISO3 = "IDN"
COUNTRY_NAME = "Indonesia"
BASE = "https://api.worldbank.org/v2"

# ---------------------------------------------------------------------------
# 17 indikator — (kode WB, label pendek, unit, kategori)
# ---------------------------------------------------------------------------
INDICATORS = [
    ("NY.GDP.MKTP.CD",      "gdp_usd",            "GDP (US$)",              "Output"),
    ("NY.GDP.MKTP.KD.ZG",   "gdp_growth_pct",     "GDP growth (%)",         "Output"),
    ("NY.GDP.PCAP.CD",      "gdp_per_capita_usd", "GDP per capita (US$)",   "Output"),
    ("SP.POP.TOTL",         "population",         "Population",             "Demography"),
    ("SP.URB.TOTL.IN.ZS",   "urban_pct",          "Urban population (%)",   "Demography"),
    ("SP.DYN.LE00.IN",      "life_expectancy",    "Life expectancy (yrs)",  "Demography"),
    ("FP.CPI.TOTL.ZG",      "inflation_pct",      "Inflation (%)",          "Prices"),
    ("SL.UEM.TOTL.ZS",      "unemployment_pct",   "Unemployment (%)",       "Labour"),
    ("SL.TLF.CACT.ZS",      "lf_participation_pct","Labour participation (%)","Labour"),
    ("IT.NET.USER.ZS",      "internet_pct",       "Internet users (%)",     "Technology"),
    ("BX.KLT.DINV.WD.GD.ZS","fdi_pct_gdp",        "FDI inflows (% GDP)",    "Investment"),
    ("NE.EXP.GNFS.ZS",      "exports_pct_gdp",    "Exports (% GDP)",        "Trade"),
    ("SE.XPD.TOTL.GD.ZS",   "education_pct_gdp",  "Education spend (% GDP)","Social"),
    ("SH.XPD.CHEX.GD.ZS",   "health_pct_gdp",     "Health spend (% GDP)",   "Social"),
    ("SI.POV.GINI",         "gini",               "Gini index",             "Inequality"),
    ("EN.GHG.CO2.MT.CE.AR5","co2_mt",             "CO2 emissions (Mt)",     "Environment"),
    ("AG.SRF.TOTL.K2",      "land_area_km2",      "Land area (km²)",        "Geography"),
]


def fetch_indicator(code: str, retries: int = 3) -> list[dict]:
    """Ambil semua tahun untuk satu indikator (pagination + retry)."""
    rows, page = [], 1
    while True:
        data = None
        for attempt in range(retries):
            try:
                r = requests.get(
                    f"{BASE}/country/{COUNTRY}/indicator/{code}",
                    params={"format": "json", "per_page": 1000, "page": page},
                    timeout=60,
                )
                r.raise_for_status()
                data = r.json()
                break
            except Exception:
                if attempt == retries - 1:
                    raise
                time.sleep(3 * (attempt + 1))
        if not isinstance(data, list) or len(data) < 2 or not data[1]:
            break
        rows.extend(data[1])
        meta = data[0]
        if page >= meta.get("pages", 1):
            break
        page += 1
        time.sleep(0.3)
    return rows


def main():
    long_rows = []
    manifest = []

    for code, short, label, cat in INDICATORS:
        try:
            rows = fetch_indicator(code)
        except Exception as e:
            print(f"  [SKIP] {code}: {e}")
            continue
        n = 0
        for item in rows:
            if item.get("value") is None:
                continue
            long_rows.append({
                "country": item["country"]["value"],
                "country_iso3": item["countryiso3code"],
                "indicator_code": code,
                "indicator": short,
                "indicator_label": label,
                "category": cat,
                "year": int(item["date"]),
                "value": item["value"],
            })
            n += 1
        manifest.append({"code": code, "short": short, "label": label,
                         "category": cat, "n_points": n})
        print(f"  [{n:>3} pts] {short:<22} {label}")
        time.sleep(0.3)

    long_df = pd.DataFrame(long_rows).sort_values(["indicator", "year"])
    long_df.to_csv(RAW / "indonesia_indicators_long.csv", index=False)

    # wide: baris = tahun, kolom = indikator
    wide = (long_df.pivot_table(index="year", columns="indicator",
                                values="value", aggfunc="first")
            .sort_index())
    wide.to_csv(PROC / "indonesia_indicators_wide.csv")

    # simpan manifest
    (RAW / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\n[OK] long: {len(long_df)} baris -> {RAW/'indonesia_indicators_long.csv'}")
    print(f"[OK] wide: {wide.shape[0]} tahun x {wide.shape[1]} indikator "
          f"({wide.index.min()}–{wide.index.max()})")


if __name__ == "__main__":
    main()
