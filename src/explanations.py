"""
explanations.py
===============
Narasi penjelasan untuk SETIAP chart & tabel di dashboard Indonesia Economy.

STANDAR WAJIB (registry E56): setiap elemen visual wajib punya
  · KENAPA   — mengapa analisis ini dipilih
  · TUJUAN   — pertanyaan bisnis yang dijawab
  · DAMPAK   — implikasi / keputusan yang timbul
  plus CARA BACA bila grafik tidak intuitif.
"""

from __future__ import annotations

EXPLAIN = {
    "gdp_pc": {
        "judul": "GDP per Kapita (1967–2025)",
        "kenapa": "GDP per kapita adalah ukuran tunggal terbaik untuk tingkat "
                  "kemakmuran rata-rata penduduk — lebih bermakna daripada GDP "
                  "total yang terdistorsi oleh jumlah penduduk.",
        "tujuan": "Melihat lintasan kemakmuran Indonesia selama ~6 dekade, "
                  "termasuk guncangan krisis yang meninggalkan bekas.",
        "dampak": "Tren naik konsisten menunjukkan transformasi ekonomi berhasil; "
                  "titik jatuh menandai kerentanan yang perlu diantisipasi "
                  "(kebijakan stabilisasi, jaring pengaman).",
        "baca": "Sumbu-Y = US$ nominal. Area abu-abu = periode krisis "
                "(1998, 2020). Semakin curam naik = pertumbuhan makin cepat.",
    },
    "growth": {
        "judul": "Pertumbuhan GDP (%)",
        "kenapa": "Angka pertumbuhan tahunan (bukan level) menunjukkan dinamika "
                  "dan seberapa sering ekonomi jatuh ke resesi.",
        "tujuan": "Mengukur frekuensi & kedalaman resesi Indonesia sepanjang sejarah.",
        "dampak": "Batang negatif = resesi. Yang paling dalam (1998) jauh lebih "
                  "parah dari COVID (2020) → pelajaran manajemen krisis.",
        "baca": "Hijau = tumbuh; merah = menyusut. Bandingkan kedalaman batang "
                "negatif antara 1998 dan 2020.",
    },
    "population_urban": {
        "judul": "Populasi & Urbanisasi",
        "kenapa": "Dua variabel demografis ini membentuk ukuran pasar tenaga kerja, "
                  "kebutuhan infrastruktur, dan basis pajak.",
        "tujuan": "Melihat seberapa cepat Indonesia berubah dari negara agraris "
                  "menjadi mayoritas urban.",
        "dampak": "Urbanisasi >50% berarti tantangan & peluang bergeser ke kota "
                  "(perumahan, transportasi, layanan digital) — prioritas investasi.",
        "baca": "Garis biru = populasi (juta); garis putus-putus hijau = % urban. "
                "Dua sumbu Y berbeda — perhatikan warnanya.",
    },
    "social": {
        "judul": "Indikator Sosial (harapan hidup & internet)",
        "kenapa": "Kemajuan ekonomi harus dibuktikan dengan kualitas hidup; dua "
                  "indikator ini mewakili kesehatan & konektivitas.",
        "tujuan": "Menilai apakah pertumbuhan ekonomi benar-benar diterjemahkan "
                  "menjadi kesejahteraan sosial.",
        "dampak": "Harapan hidup & adopsi internet yang melesat menandakan fondasi "
                  "SDM kuat untuk ekonomi digital — dasar kebijakan investasi "
                  "teknologi & kesehatan.",
        "baca": "Panel kiri = harapan hidup (tahun); kanan = pengguna internet (%).",
    },
    "correlation": {
        "judul": "Matriks Korelasi Antar-Indikator",
        "kenapa": "Indikator ekonomi saling terhubung; korelasi mengungkap pola "
                  "pembangunan yang konsisten (atau anomali).",
        "tujuan": "Melihat indikator mana yang bergerak bersama sebagai satu "
                  "'paket pembangunan'.",
        "dampak": "Korelasi kuat (mis. GDP↔harapan hidup↔internet) menunjukkan "
                  "kebijakan pada satu bidang berdampak pada yang lain. "
                  "INGAT: korelasi ≠ sebab-akibat.",
        "baca": "Warna merah = negatif, biru/hijau = positif; semakin mendekati "
                "±1 semakin kuat. Nilai di dalam sel = koefisien.",
    },
    "forecast": {
        "judul": "Peramalan GDP per Kapita",
        "kenapa": "Perencanaan jangka panjang (anggaran, target pembangunan) "
                  "membutuhkan proyeksi, bukan hanya data historis.",
        "tujuan": "Memproyeksikan GDP per kapita beberapa tahun ke depan "
                  "beserta tingkat keandalan modelnya.",
        "dampak": "Bila proyeksi menunjukkan akselerasi (atau stagnasi), "
                  "pemerintah/pelaku usaha harus menyesuaikan strategi. Angka "
                  "MAPE menandakan seberapa jauh proyeksi boleh dipercaya.",
        "baca": "Garis gelap = aktual; garis merah putus-putus = ramalan; "
                "band = ketidakpastian ±5%. R² tinggi = model patuh data historis.",
    },
    "eras": {
        "judul": "Perbandingan Era Ekonomi",
        "kenapa": "Rata-rata tunggal menyembunyikan perbedaan antar-rezim "
                  "kebijakan; memecah per era menunjukkan lompatan & perlambatan.",
        "tujuan": "Membandingkan kinerja tiap era (Orde Baru, krisis, boom "
                  "komoditas, COVID) untuk menilai dampak kebijakan/peristiwa.",
        "dampak": "Menunjukkan era mana yang paling produktif dalam menaikkan "
                  "kemakmuran — referensi penting untuk kebijakan sekarang.",
        "baca": "Panjang batang = rata-rata GDP/kapita era. Rentang (min–max) "
                "menunjukkan volatilitas dalam era tersebut.",
    },
    "industries": {
        "judul": "Kontribusi Sektor (bila tersedia)",
        "kenapa": "Struktur ekonomi penting: apakah bergantung pada komoditas "
                  "atau terdiversifikasi?",
        "tujuan": "Memahami bauran sektor ekonomi sebagai konteks pertumbuhan.",
        "dampak": "Ketergantungan tinggi pada satu sektor = kerentanan; "
                  "diversifikasi = ketahanan.",
        "baca": "Proporsi tiap sektor terhadap total.",
    },
    "kpi": {
        "judul": "Ringkasan Indikator Kunci",
        "kenapa": "Pembaca perlu gambaran cepat sebelum masuk ke analisis detail.",
        "tujuan": "Menyajikan metrik paling penting (GDP/kapita, populasi, "
                  "inflasi, urbanisasi, internet) dalam satu pandangan.",
        "dampak": "Dasar cepat untuk diskusi & keputusan; perubahan antar-filter "
                  "menunjukkan sensivitas.",
        "baca": "Setiap kartu menampilkan nilai terkini + konteks historisnya.",
    },
}


def text(key: str) -> str:
    e = EXPLAIN.get(key)
    if not e:
        return ""
    parts = [f"**{e['judul']}**",
             f"- **Kenapa:** {e['kenapa']}",
             f"- **Tujuan:** {e['tujuan']}",
             f"- **Dampak:** {e['dampak']}"]
    if e.get("baca"):
        parts.append(f"- **Cara baca:** {e['baca']}")
    return "\n".join(parts)


def render(key: str, expanded: bool = False, st=None):
    if st is None:
        import streamlit as st  # noqa
    e = EXPLAIN.get(key)
    if not e:
        return
    with st.expander(f"💡 {e['judul']} — Kenapa · Tujuan · Dampak", expanded=expanded):
        st.markdown(
            f"**🔎 Kenapa** — {e['kenapa']}\n\n"
            f"**🎯 Tujuan** — {e['tujuan']}\n\n"
            f"**📈 Dampak** — {e['dampak']}")
        if e.get("baca"):
            st.caption(f"👁️ Cara baca: {e['baca']}")


def audit() -> dict:
    return {k: all(v.get(f) for f in ("kenapa", "tujuan", "dampak"))
            for k, v in EXPLAIN.items()}


if __name__ == "__main__":
    ok = audit()
    print(f"Penjelasan: {len(ok)} | lengkap: {sum(ok.values())}")
    for k, v in ok.items():
        print(f"  {'OK ' if v else 'MISSING'} {k}")
