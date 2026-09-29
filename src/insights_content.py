
# ---------------------------------------------------------------------------
# KONTEN INSIGHT — Indonesia Economy Intelligence
# Sudut pandang: perencana kebijakan ekonomi / analis investasi makro.
# ---------------------------------------------------------------------------
from insight import register

register(
    "gdp_pc",
    kesimpulan=(
        "GDP per kapita Indonesia tumbuh konsisten sejak 1967 hingga 2025, "
        "melewati beberapa krisis (1998, 2008, 2020) dengan pemulihan. Tren "
        "jangka panjang positif, tetapi laju melambat dalam satu dekade terakhir "
        "— tanda transisi dari ekonomi berkembang cepat ke kematangan."),
    rekomendasi=[
        "Fokus kebijakan pada NAIK KELAS: dorong produktivitas (pendidikan, "
        "teknologi) karena pertumbuhan berbasis tenaga kerja murah mulai habis.",
        "Bangun bantalan fiskal/valas yang lebih tebal — data menunjukkan krisis "
        "datang berkala (1998, 2008, 2020).",
        "Jaga stabilitas untuk menarik investasi jangka panjang; volatilitas "
        "menggerus kepercayaan.",
    ],
    risiko=(
        "Middle-income trap: bila produktivitas tidak naik sementara biaya "
        "meningkat, Indonesia bisa stagnan di level menengah. Perlambatan yang "
        "diabaikan akan berujung pada pertumbuhan mendekati nol."),
    tingkat="tinggi",
)

register(
    "growth",
    kesimpulan=(
        "Pertumbuhan GDP sangat volatil: lonjakan tinggi di masa booming, "
        "kontraksi tajam di 1998 & 2020. Pola ini menunjukkan ekonomi Indonesia "
        "RENTAN terhadap guncangan eksternal, dengan pemulihan cepat setelahnya."),
    rekomendasi=[
        "Perkuat sistem jaring pengaman otomatis (stabilizer) — krisis berulang, "
        "respons harus cepat tanpa menunggu keputusan lambat.",
        "Diversifikasi ekonomi agar tidak bergantung pada satu sektor/komoditas "
        "yang rentan guncangan global.",
        "Dokumentasikan playbook pemulihan pasca-1998 & 2020 sebagai rujukan krisis berikutnya.",
    ],
    risiko=(
        "Tanpa stabilizer & diversifikasi, krisis berikutnya akan memukul lebih "
        "keras. Ketergantungan pada komoditas membuat ekonomi tersandera siklus "
        "harga global."),
    tingkat="tinggi",
)

register(
    "population_urban",
    kesimpulan=(
        "Populasi tumbuh seiring urbanisasi cepat. Pergeseran ke kota menandakan "
        "transisi struktural dari pertanian ke industri/jasa — pendorong "
        "pertumbuhan, sekaligus sumber masalah baru (kepadatan, informalitas, "
        "kesenjangan kota-desa)."),
    rekomendasi=[
        "Investasi infrastruktur kota (transportasi, perumahan, air) mengikuti "
        "laju urbanisasi agar tidak menimbulkan krisis perkotaan.",
        "Siapkan transisi tenaga kerja dari pertanian ke sektor produktif "
        "(pelatihan ulang, akses kredit).",
        "Antisipasi kesenjangan kota-desa — jangan biarkan desa tertinggal dalam "
        "arus urbanisasi.",
    ],
    risiko=(
        "Urbanisasi yang tidak dikelola menghasilkan permukiman kumuh, "
        "pengangguran kota, & kesenjangan. Bonus demografi bisa berubah menjadi "
        "beban bila lapangan kerja tidak siap."),
    tingkat="sedang",
)

register(
    "social",
    kesimpulan=(
        "Harapan hidup & penetrasi internet naik seiring pertumbuhan ekonomi. "
        "Peningkatan kualitas hidup ini menunjukkan pertumbuhan berdampak — "
        "tetapi kesenjangan antar-daerah mungkin tersembunyi di angka nasional."),
    rekomendasi=[
        "Pantau indikator sosial PER DAERAH — rata-rata nasional menyembunyikan "
        "ketimpangan (Papua, NTT sering tertinggal).",
        "Alokasikan investasi pada pendidikan & kesehatan di wilayah dengan "
        "indikator sosial terendah.",
        "Digitalisasi (internet) sebagai katalis pemerataan — dorong akses ke "
        "daerah 3T (terdepan, terluar, tertinggal).",
    ],
    risiko=(
        "Indikator sosial yang membaik di rata-rata nasional bisa tetap buruk di "
        "daerah tertentu. Ketimpangan infrastruktur digital memperlebar jurang "
        "pendidikan & ekonomi antar-wilayah."),
    tingkat="sedang",
)

register(
    "correlation",
    kesimpulan=(
        "Matriks korelasi mengungkap hubungan antar-indikator: pertumbuhan, "
        "infrastruktur, dan indikator sosial saling terkait. Korelasi tidak "
        "berarti KAUSALITAS — dua hal bergerak bersama bukan berarti satu "
        "menyebabkan yang lain."),
    rekomendasi=[
        "Gunakan korelasi untuk HIPOTESIS, bukan kesimpulan — uji kausalitas "
        "sebelum mengambil kebijakan.",
        "Waspadai confounding: GDP, internet, & harapan hidup semuanya naik "
        "karena waktu — korelasinya bisa semu (spurious).",
        "Fokus pada hubungan yang kuat DAN masuk akal secara teori ekonomi.",
    ],
    risiko=(
        "Mengambil kebijakan dari korelasi semu (mis. 'tingkatkan internet untuk "
        "naikkan GDP') bisa menyesatkan alokasi. Hubungan statistik tanpa teori "
        "= dasar kebijakan yang rapuh."),
    tingkat="tinggi",
)

register(
    "forecast",
    kesimpulan=(
        "Peramalan GDP memproyeksikan tren ke depan, tetapi hasilnya bergantung "
        "pada asumsi & rentang data. Proyeksi jangka sangat panjang cenderung tak "
        "realistis bila mengabaikan batas struktur ekonomi."),
    rekomendasi=[
        "Baca proyeksi sebagai SKENARIO (optimis/basis/pesimis), bukan ramalan pasti.",
        "Batasi horizon proyeksi — tingkat ketidakpastian tumbuh cepat seiring waktu.",
        "Sertakan asumsi eksplisit & batas kepercayaan; jangan sampaikan satu "
        "angka tanpa rentang.",
    ],
    risiko=(
        "Proyeksi yang disajikan sebagai 'kepastian' dapat menyesatkan kebijakan "
        "investasi/pinjaman. Keputusan berbasis proyeksi tak terverifikasi "
        "berisiko kerugian besar."),
    tingkat="tinggi",
)

register(
    "eras",
    kesimpulan=(
        "Perbandingan era menegaskan pola: \u2014era REPELITA\u2014 (pembangunan "
        "cepat), \u2014era krisis\u2014 (1998), dan \u2014era reformasi\u2014 "
        "(pertumbuhan stabil tapi lebih rendah). Setiap era punya karakter & "
        "pelajaran berbeda."),
    rekomendasi=[
        "Pelajari era pertumbuhan tinggi (1970-90an) untuk faktor pendorongnya, "
        "tetapi jangan replikasi (konteks sudah berubah).",
        "Dari era krisis: identifikasi kerentanan struktural yang harus dihindari.",
        "Tetapkan target era saat ini berbasis realitas (fondasi makro), bukan "
        "nostalgia era lain.",
    ],
    risiko=(
        "Mengejar pertumbuhan era lama tanpa memahami perbedaan konteks = target "
        "takrealistis. Kebijakan berbasis nostalgia bisa mengabaikan tantangan "
        "baru (digitalisasi, iklim, demografi)."),
    tingkat="sedang",
)
