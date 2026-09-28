<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=42&duration=3000&pause=1000&color=C0392B&center=true&vCenter=true&width=900&height=70&lines=INDONESIA+ECONOMIC+INTELLIGENCE" alt="Indonesia Economic Intelligence" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=16&duration=2500&pause=800&color=C0392B&center=true&vCenter=true&multiline=true&width=940&height=50&lines=60%2B+Years+%E2%86%92+17+Indicators+%E2%86%92+Analysis+%E2%86%92+Forecast+%E2%86%92+Dashboard" alt="Tagline" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-C0392B?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://indonesia-economy-intelligence-ffxgbkhxnsptmc8g5p3pqj.streamlit.app/)
[![Open Dashboard](https://img.shields.io/badge/%E2%96%B6_Live_Demo-Open_Dashboard-00C853?style=for-the-badge)](https://indonesia-economy-intelligence-ffxgbkhxnsptmc8g5p3pqj.streamlit.app/)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![World Bank](https://img.shields.io/badge/World_Bank-Open_Data-0071BC?style=for-the-badge)
![Coverage](https://img.shields.io/badge/Coverage-1960%E2%80%932025-C0392B?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-0D1117?style=for-the-badge)

</div>

---

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║   ██╗███╗   ██╗██████╗  ██████╗ ███╗   ██╗███████╗███████╗██╗ █████╗     ║
║   ██║████╗  ██║██╔══██╗██╔═══██╗████╗  ██║██╔════╝██╔════╝██║██╔══██╗    ║
║   ██║██╔██╗ ██║██║  ██║██║   ██║██╔██╗ ██║█████╗  ███████╗██║███████║    ║
║   ██║██║╚██╗██║██║  ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║██║██╔══██║    ║
║   ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚████║███████╗███████║██║██║  ██║    ║
║   ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝╚═╝  ╚═╝    ║
║                                                                          ║
║   ECONOMY INTELLIGENCE · 17 INDICATORS · 1960–2025 · FORECAST TO 2030    ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🎬 Demo

<div align="center">

### ▶️ [**Buka Live Dashboard →**](https://indonesia-economy-intelligence-ffxgbkhxnsptmc8g5p3pqj.streamlit.app/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://indonesia-economy-intelligence-ffxgbkhxnsptmc8g5p3pqj.streamlit.app/)

<img src="reports/figures/dashboard_trends.png" width="880" alt="Indonesia Economic Dashboard" />
<br/>
<sub><i>Interactive Streamlit dashboard — Trends · Comparison · Forecast · Crisis tabs · 17 indicators · 1960–2025</i></sub>

</div>

<br/>

**Run locally:**

```bash
streamlit run app/dashboard.py     # → http://localhost:8502
```

---

## 🧠 Overview

**Indonesia Economic Intelligence** is an end-to-end data analyst project: it pulls
**60+ years of Indonesia's national statistics** from the World Bank Open Data API
(public & free), cleans them, analyses them across economic eras, and **forecasts
them five years ahead** — delivered as an interactive dashboard and a business report.

<div align="center">

| Metric | Value |
|-------:|:------|
| 📊 Source | World Bank Open Data (public API) |
| 📅 Coverage | **1960–2025** (66 years) |
| 🧩 Indicators | **17** (GDP, inflation, population, social, environment) |
| 📈 Records | 874 data points |
| 🔮 Forecast | 2026–2030 with backtest MAPE |
| 🖥️ Deliverables | Streamlit app · 8 charts · 14 insight tables · business `REPORT.md` |
| 📁 Outputs | `reports/figures/` · `reports/tables/` · `reports/summary.json` |

</div>

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│              collect_worldbank.py  (World Bank Open Data API)         │
│   17 indicators · pagination + retry · raw long + wide format         │
└──────────────────────────────┬───────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        analysis.py                                   │
│   cross-era summary · crisis impact · correlation matrix             │
│   key insights (CAGR, peaks, structural shift)                       │
└───────────────┬───────────────────────────────┬──────────────────────┘
                │                               │
                ▼                               ▼
┌───────────────────────────┐       ┌───────────────────────────────┐
│   forecast.py             │       │   make_charts.py              │
│   log / linear / damped / │       │   8 static PNG charts         │
│   mean-rev + backtest MAPE│       │   (report / slides)           │
└───────────────────────────┘       └───────────────────────────────┘
                │                               │
                └───────────────┬───────────────┘
                                ▼
                  🇮🇩 app/dashboard.py — Streamlit + Plotly (4 tabs)
```

---

## ⚡ Technical Challenges Solved

### Challenge 1 — Forecasting with the *Right* History

**Problem:** Forecasting GDP using the **entire** series (1967–2025) produced
**+117% in 5 years** — absurd, because it mixed in the high-growth New Order era
that has long ended.

**Solution:** Restrict the model to the **recent regime** (2010+). Result: a realistic
**+19%** over 5 years, and backtest MAPE dropped from **35% → 6.4%**.

```python
# ❌ Whole history (1967+) → explosive, unrealistic projection
# ✅ Recent regime (2010+)  → realistic trend
"gdp_usd": ("log", 2010),        # not 1967
```

---

### Challenge 2 — One Model Does NOT Fit All Indicators

**Problem:** A single linear trend mis-forecasts indicators with different shapes —
internet adoption (S-curve) and inflation (volatile) especially.

**Solution:** **Per-indicator model selection**:

```python
log       -> exponential growth    (GDP, population)
linear    -> stable trend          (urbanisation, life expectancy)
damped    -> S-curve saturation    (internet adoption, phi=0.85/yr)
mean_rev  -> volatile series       (inflation)
```

Internet forecast error dropped **39% → 19.8%** when switched from linear to damped.

---

### Challenge 3 — Proving Forecast Quality (Not Just Claiming It)

**Problem:** Anyone can draw a line into the future. The analyst must show *how good*
it is.

**Solution:** **Walk-forward backtesting** → mean absolute percentage error (MAPE)
per indicator, reported honestly — including the indicators where the model does
**poorly** (inflation, MAPE 52.8%, by nature volatile).

---

### Challenge 4 — Robust Public-API Ingestion

**Problem:** World Bank API returns nulls, paginates, and can time out. Its search
endpoint even **ignores the query** (returns the same result for "GDP" and "inflation").

**Solution:** Retry + timeout, filter nulls, paginate via `meta.pages`, store data in
**both long and wide** form — and use **known indicator codes** rather than trusting search.

---

## 📊 Key Findings

<div align="center">

| # | Finding | Numbers |
|---|---------|---------|
| F1 | GDP per capita grew **~95×** since 1967 | $53 → **$5,060** (2025) · CAGR 8.17% |
| F2 | Hyperinflation tamed into stability | **1,136%** (1966) → **1.9%** (2025) |
| F3 | Structural shift to urban | urbanisation **14.6% → 59.4%** |
| F4 | Fast digital transformation | internet **0.9% → 72.8%** |
| F5 | 1998 hit far harder than COVID | GDP **−13.1%** (1998) vs −2.1% (2020) |
| F6 | Social progress: +24 life-years | **46.8 → 71.3** years |

</div>

| GDP per capita (1967–2025) | Growth & crises |
|:---:|:---:|
| ![gdp](reports/figures/01_gdp_per_capita.png) | ![growth](reports/figures/02_gdp_growth.png) |

| Inflation (log scale) | Population & urbanisation |
|:---:|:---:|
| ![inflation](reports/figures/03_inflation.png) | ![pop](reports/figures/04_population_urban.png) |

| Social indicators | Correlation matrix |
|:---:|:---:|
| ![social](reports/figures/05_social_indicators.png) | ![corr](reports/figures/06_correlation.png) |

| GDP per capita forecast | Era comparison |
|:---:|:---:|
| ![forecast](reports/figures/07_forecast_gdp_pc.png) | ![eras](reports/figures/08_eras.png) |

---

## 🔮 Forecasting (2026–2030)

| Indicator | Method | R² | MAPE | 2030 forecast |
|-----------|--------|----:|-----:|---------------|
| GDP (US$) | log-trend | 0.93 | **6.4%** | ~$1.72 T (+19%) |
| GDP per capita | log-trend | 0.87 | **7.1%** | ~$5,703 |
| Population | log-trend | 0.99 | **3.0%** | ~313.6 M |
| Urbanisation | linear | 0.98 | **3.1%** | ~65.0% |
| Life expectancy | linear | 0.93 | **2.2%** | ~72.9 yrs |
| Internet | damped | 0.92 | 19.8% | ~78.9% |
| Inflation | mean-reverting | 0.64 | ⚠️ 52.8% | ~2.9% |

> ⚠️ Inflation is genuinely hard to forecast (high backtest error) — reported as-is,
> not hidden.

---

## 📁 File Structure

```
indonesia-economy-intelligence/
├── app/
│   ├── dashboard.py                 # ⭐ Interactive Streamlit dashboard
│   └── .streamlit/config.toml
├── src/
│   ├── collect_worldbank.py         # pull 17 indicators from World Bank API
│   ├── analysis.py                  # trends, eras, correlation, crisis impact
│   ├── forecast.py                  # multi-method forecasting + backtest
│   ├── run_analysis.py              # orchestrator (tables + summary.json)
│   └── make_charts.py               # 8 visualisations
├── data/
│   ├── raw/                         # World Bank long-format data
│   └── processed/                   # wide-format (year × indicator)
├── reports/
│   ├── figures/                     # 8 charts + dashboard screenshots
│   ├── tables/                      # 14 insight tables
│   └── summary.json                 # headline metrics & insights
├── REPORT.md                        # full business report
├── .streamlit/config.toml           # theme (Cloud reads from root)
└── requirements.txt
```

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/SandiRidwan/indonesia-economy-intelligence.git
cd indonesia-economy-intelligence
pip install -r requirements.txt
```

### 2. Pull Data & Analyse

```bash
python src/collect_worldbank.py    # World Bank API → data/
python src/run_analysis.py         # insight tables + summary.json
python src/make_charts.py          # 8 charts
```

### 3. Run the Dashboard

```bash
streamlit run app/dashboard.py     # → http://localhost:8502
```

---

## 📊 Live Run Results

```
Pipeline run — Indonesia Economic Intelligence

✅ Collect  17 indicators from World Bank API
               → 874 records · 1960–2025 (66 years)
✅ Analyse  cross-era · crisis impact · correlation matrix
✅ Forecast 8 indicators · 5-year horizon · backtest MAPE
✅ Charts   8 visualisations generated
✅ Report   REPORT.md + 14 insight tables + summary.json
✅ App      Streamlit dashboard — 4 tabs, interactive filters
──────────────────────────────────────────────────────────────
   Deliverables: report · charts · dashboard · forecast with metrics
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.10+ |
| **Data** | pandas · numpy |
| **Source** | World Bank Open Data API |
| **Forecasting** | custom log / linear / damped / mean-reverting models |
| **Validation** | walk-forward backtest (MAPE) |
| **Visualisation** | matplotlib · Plotly |
| **Dashboard** | Streamlit |

</div>

---

## 🏆 Why This Matters

<div align="center">

| Capability | Companies Hiring For It | Market Value |
|---|---|---|
| Economic / macro analysis | Banks, consultancies, government, think tanks | $50–100/hr |
| Time-series forecasting | Every data-driven org | $50–110/hr |
| Data storytelling (public data) | Media, NGOs, strategy teams | $40–80/hr |
| **Full chain: API → analysis → forecast → dashboard** | Rare combined skillset | **$75–150/hr** |

</div>

This project proves the analyst's *whole* workflow on credible public data:
ingesting from an API, reasoning across 60 years, forecasting with honest
validation, and shipping a dashboard a stakeholder can explore.

---

## 📝 Lessons Learned

1. **Forecast with the relevant regime, not all history.** Full-history GDP trends
   gave unrealistic +117%/5yr; using 2010+ fixed it to +19%.
2. **Match the model to the indicator.** Exponential, linear, damped and
   mean-reverting series each need their own treatment.
3. **Backtest or it didn't happen.** Report MAPE — including the bad ones.
4. **Public APIs misbehave.** Nulls, pagination, timeouts, and search endpoints that
   ignore your query — always verify.
5. **Korrelation ≠ causation.** The heatmap shows association, not cause.

---

## ⚠️ Limitations (Honest Disclosure)

1. Recent World Bank years may include **projections**, not final figures.
2. **Inflation forecasting is unreliable** (high MAPE) due to inherent volatility.
3. Correlation is **not** causation.
4. Coverage is limited to 17 macro indicators.

---



---

## 📖 Cara Membaca Dashboard (Kenapa · Tujuan · Dampak)

Setiap chart & tabel di dashboard ini dilengkapi **kotak penjelasan** yang menjawab
tiga hal — sesuai standar analisis profesional:

| Pertanyaan | Arti |
|-----------|------|
| **🔎 Kenapa** | Mengapa metrik/analisis ini dipilih (masalah & konteks) |
| **🎯 Tujuan** | Pertanyaan bisnis apa yang dijawab |
| **📈 Dampak** | Implikasi / keputusan / tindakan yang timbul |
| **👁️ Cara baca** | Panduan membaca grafik bila tidak intuitif |

Klik kotak **"💡 … — Kenapa · Tujuan · Dampak"** di atas tiap grafik untuk membukanya.
Narasi tersimpan di `src/explanations.py` (terpisah, konsisten, dapat diaudit).

## 👤 Author

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=20&duration=3000&pause=1000&color=C0392B&center=true&vCenter=true&width=400&lines=Sandi+Ridwan" />

**Data Analyst · Data Automation Engineer · Python**

📍 Palu, Central Sulawesi, Indonesia

[![Upwork](https://img.shields.io/badge/Upwork-Hire_Me-C0392B?style=for-the-badge&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~011f6d0fbb4a372974)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sandi-ridwan)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SandiRidwan)

</div>

---

<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=12&duration=4000&pause=1000&color=C0392B&center=true&vCenter=true&width=780&lines=60%2B+years+%7C+17+indicators+%7C+analysed+%7C+forecast+%7C+dashboarded+%7C+turning+public+data+into+decisions" />
</div>

---

## 📄 License

MIT License — Educational and portfolio purposes only · Data: World Bank Open Data.
