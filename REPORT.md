# 📊 Indonesia Economic Intelligence — Laporan Analitik

**Analisis 60+ tahun ekonomi Indonesia (1960–2025) dari World Bank Open Data**

> Studi data analyst end-to-end: 17 indikator makro → pembersihan → analisis
> lintas-era → peramalan → dashboard interaktif.

---

## 1. Ringkasan Eksekutif

Indonesia mengalami transformasi ekonomi luar biasa dalam 6 dekade terakhir:
dari negara berpendapatan sangat rendah pasca-kemerdekaan menjadi ekonomi
terbesar di Asia Tenggara. Laporan ini mengukur transformasi tersebut dengan
**bukti kuantitatif** dan mengidentifikasi pola yang dapat ditindaklanjuti.

**3 temuan utama:**

1. **Pertumbuhan luar biasa, tapi melambat.** GDP per kapita naik 95× sejak
   1967, namun laju pertumbuhan menurun dari puncak era Orde Baru.
2. **Dua guncangan hebat.** Krisis 1998 (GDP −13,1%) jauh lebih dalam daripada
   COVID-19 2020 (−2,1%), tetapi pemulihan pasca-COVID lebih cepat.
3. **Transformasi struktural & digital berlangsung cepat.** Urbanisasi dan
   adopsi internet mengubah lanskap ekonomi secara fundamental.

---

## 2. Data & Metodologi

| Aspek | Detail |
|-------|--------|
| **Sumber** | World Bank Open Data (API publik `api.worldbank.org`) |
| **Cakupan** | Indonesia (IDN), 1960–2025 |
| **Indikator** | 17 (output, demografi, harga, tenaga kerja, sosial, lingkungan) |
| **Bentuk data** | Long (874 baris) & Wide (66 tahun × 17 indikator) |
| **Peramalan** | Log-trend / linear / damped / mean-reversion per indikator |
| **Validasi** | Backtest walk-forward → MAPE |

**Indikator yang dianalisis:** GDP, GDP growth, GDP per kapita, populasi,
urbanisasi, harapan hidup, inflasi, pengangguran, partisipasi angkatan kerja,
pengguna internet, FDI, ekspor, belanja pendidikan, belanja kesehatan, Gini,
emisi CO2, luas daratan.

---

## 3. Temuan

### 3.1 Pertumbuhan Jangka Panjang

![GDP per kapita](../reports/figures/01_gdp_per_capita.png)

- GDP per kapita: **$53 (1967) → $5.060 (2025)** — naik **~95×**
- CAGR 1967–2025 = **8,17%** per tahun (nominal US$)
- Terlihat jelas: **lonjakan era boom komoditas 2000-an**, terhenti sejak 2013

### 3.2 Krisis Ekonomi

![GDP growth](../reports/figures/02_gdp_growth.png)

| Krisis | Dampak GDP | Inflasi |
|--------|-----------|---------|
| **1998 (Asia)** | **−13,1%** | 58,4% |
| **2020 (COVID)** | −2,1% | 1,9% |

Krisis 1998 **6× lebih dalam** dari COVID-19. Namun pemulihan pasca-COVID
(2021–2022) jauh lebih cepat berkat fundamental ekonomi yang lebih kuat.

### 3.3 Stabilitas Harga

![Inflasi](../reports/figures/03_inflation.png)

- Puncak hiperinflasi: **1.136% (1966)** — masa paling kacau
- Era modern: inflasi terkendali **~2–4%**, terendah 1,56% (2021)

### 3.4 Transformasi Struktural

![Populasi & urbanisasi](../reports/figures/04_population_urban.png)

- Penduduk: **88,3 juta → 285,7 juta**
- Urbanisasi: **14,6% → 59,4%** — Indonesia kini **mayoritas urban**

### 3.5 Kemajuan Sosial

![Indikator sosial](../reports/figures/05_social_indicators.png)

- Harapan hidup: **46,8 → 71,3 tahun** (+24,5 tahun)
- Internet: **0,9% (2000) → 72,8% (2024)** — salah satu adopsi tercepat di dunia

### 3.6 Korelasi Antar-Indikator

![Korelasi](../reports/figures/06_correlation.png)

Korelasi kuat (positif) antar indikator pembangunan: GDP per kapita, harapan
hidup, urbanisasi, dan internet saling berkorelasi tinggi — konsisten dengan
pola pembangunan global.

> ⚠️ Korelasi ≠ kausalitas.

---

## 4. Peramalan (2026–2030)

![Forecast GDP per kapita](../reports/figures/07_forecast_gdp_pc.png)

| Indikator | Metode | R² | MAPE | Prediksi 2030 |
|-----------|--------|----:|-----:|---------------|
| GDP (US$) | log | 0,93 | 6,4% | ~$1,72 T (+19%) |
| GDP per kapita | log | 0,87 | 7,1% | ~$5.703 (+13%) |
| Populasi | log | 0,99 | 3,0% | ~313,6 jt (+10%) |
| Urbanisasi | linear | 0,98 | 3,1% | ~65,0% |
| Harapan hidup | linear | 0,93 | 2,2% | ~72,9 thn |
| Internet | damped | 0,92 | 19,8% | ~78,9% |
| Inflasi | mean-rev | 0,64 | ⚠️ 52,8% | ~2,9% |

**Catatan metodologis penting:**
Percobaan awal memakai data 1967–2025 untuk meramal GDP menghasilkan
proyeksi **+117% dalam 5 tahun** — tidak realistis, karena memasukkan era
pertumbuhan tinggi (Orde Baru) yang sudah berakhir. Model diperbaiki dengan
**membatasi ke rezim terkini (2010+)** → hasil masuk akal (+19%) dan MAPE
turun dari 35% ke **6,4%**.

---

## 5. Perbandingan Era

![Era](../reports/figures/08_eras.png)

| Era | Rata-rata GDP per kapita | Karakter |
|-----|-------------------------:|----------|
| 1967–1997 Orde Baru | $457 | Pertumbuhan dari basis rendah |
| 1998–1999 Krisis Asia | $556 | Guncangan berat |
| 2000–2013 Boom komoditas | $1.954 | Akselerasi tercepat |
| 2014–2019 Perlambatan | $3.670 | Pertumbuhan melandai |
| 2020–2021 COVID | $4.070 | Resesi singkat |
| 2022–2025 Pemulihan | $4.898 | Kembali ke jalur |

---

## 6. Rekomendasi

| # | Rekomendasi | Dasar |
|---|-------------|-------|
| R1 | **Diversifikasi ekonomi** di luar komoditas | Perlambatan pasca-2013 & boom komoditas berakhir |
| R2 | **Manfaatkan bonus demografi & urbanisasi** | 59% urban, populasi muda besar |
| R3 | **Perkuat jaring sosial** sebelum perlambatan | Gini naik (~35), ketimpangan perlu dipantau |
| R4 | **Akselerasi ekonomi digital** | Internet 72,8% = basis kuat |
| R5 | **Jaga stabilitas harga** | Keberhasilan inflasi rendah = fondasi |

---

## 7. Keterbatasan

1. Data World Bank 2024–2025 dapat berisi proyeksi, bukan angka final
2. Peramalan inflasi tidak reliabel (MAPE tinggi) — volatilitas alami
3. Korelasi bukan kausalitas
4. Hanya 17 indikator makro; dinamika sektoral tidak tercakup

---

*Dibuat oleh Sandi Ridwan · portofolio data analyst · sumber: World Bank Open Data*
