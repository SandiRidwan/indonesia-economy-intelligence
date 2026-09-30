
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
        {
            "aksi": "Naik kelas dari pertumbuhan berbasis tenaga kerja murah ke produktivitas",
            "langkah": [
                "Petakan gap GDP per kapita Indonesia (US$) terhadap ambang middle-income trap — dari ~$800 (1967) ke level saat ini dalam seri 1960–2025.",
                "Geser belanja dari input fisik ke kualitas SDM: alokasi anggaran pendidikan & riset naik bertahap menuju 20% APBN yang produktif.",
                "Targetkan kenaikan value-added industri pengolahan (bukan ekspor bahan mentah) dengan insentif hilirisasi terukur per sektor.",
            ],
            "metrik": "GDP per kapita (US$) & laju pertumbuhannya per tahun, dibandingkan garis ambang middle-income",
            "pemilik": "Kementerian Keuangan & Bappenas",
        },
        {
            "aksi": "Pertebal bantalan fiskal & cadangan devisa untuk krisis berkala",
            "langkah": [
                "Tandai tiga titik krisis pada seri GDP per kapita sebagai referensi: 1998 (kontraksi terdalam), 2008, dan 2020.",
                "Tetapkan lantai cadangan devisa (dalam bulan impor) dan ruang fiskal minimum saat kondisi normal.",
                "Bangun mekanisme penarikan cepat (contingency fund) yang diuji tiap tahun terhadap skenario krisis-1998.",
            ],
            "metrik": "Cadangan devisa (bulan impor), defisit fiskal (% PDB), & rentang ruang fiskal",
            "pemilik": "Bank Indonesia & Kementerian Keuangan",
        },
        {
            "aksi": "Jaga stabilitas makro untuk menarik investasi jangka panjang",
            "langkah": [
                "Redam volatilitas nilai tukar & inflasi yang menggerus kepercayaan investor pada seri 1960–2025.",
                "Publikasikan kalender reformasi struktural agar ketidakpastian kebijakan menurun.",
                "Sambungkan stabilitas dengan insentif FDI (kemudahan izin, kepastian hukum) untuk menaikkan modal jangka panjang.",
            ],
            "metrik": "Volatilitas nilai tukar & inflasi (%), arus FDI neto (% PDB)",
            "pemilik": "Bank Indonesia & BKPM",
        },
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
        {
            "aksi": "Perkuat stabilizer otomatis agar respons krisis tidak menunggu keputusan lambat",
            "langkah": [
                "Identifikasi dua kontraksi tajam pada seri pertumbuhan (1998 & 2020) sebagai pemicu (trigger) otomatis.",
                "Rancang jaring pengaman otomatis (bansos, asuransi pengangguran) yang aktif saat pertumbuhan turun melewati ambang tertentu.",
                "Uji kecepatan aktivasi mekanisme ini terhadap pola pemulihan pasca-1998 & pasca-2020.",
            ],
            "metrik": "Waktu aktivasi respons (hari) & laju pemulihan pertumbuhan GDP (%) pasca-krisis",
            "pemilik": "Kementerian Keuangan & Bappenas",
        },
        {
            "aksi": "Diversifikasi ekonomi dari ketergantungan komoditas",
            "langkah": [
                "Kaitkan lonjakan pertumbuhan era boom komoditas (2000–2013) dengan harga komoditas global untuk mengukur eksposur.",
                "Petakan konsentrasi ekspor per sektor & ukur indeks keragaman ekspor.",
                "Kembangkan sektor padat-produktivitas (manufaktur, jasa digital) dengan target kontribusi PDB eksplisit per tahun.",
            ],
            "metrik": "Indeks keragaman ekspor & kontribusi sektor non-komoditas terhadap PDB (%)",
            "pemilik": "Kementerian Perdagangan & Kementerian Perindustrian",
        },
        {
            "aksi": "Dokumentasikan playbook pemulihan pasca-krisis sebagai rujukan",
            "langkah": [
                "Ekstrak kronologi kebijakan yang bekerja pada pemulihan 1998 dan 2020 dari seri pertumbuhan 1960–2025.",
                "Ubah menjadi protokol respons bertahap (fase darurat, stabilisasi, pemulihan) yang diuji lewat simulasi.",
                "Simpan sebagai rujukan terpadu lintas lembaga untuk krisis berikutnya.",
            ],
            "metrik": "Kelengkapan protokol (fase teruji) & MAPE proyeksi pemulihan vs realisasi",
            "pemilik": "Bappenas & Sekretariat Kabinet",
        },
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
        {
            "aksi": "Sinkronkan investasi infrastruktur kota dengan laju urbanisasi",
            "langkah": [
                "Proyeksikan laju urbanisasi 1960–2025 ke depan untuk menghitung kebutuhan kota tambahan per tahun.",
                "Ikat anggaran transportasi, perumahan, dan air bersih pada proyeksi laju urbanisasi (bukan jumlah penduduk statis).",
                "Siapkan ambang kepadatan yang memicu percepatan pembangunan infrastruktur.",
            ],
            "metrik": "Rasio urbanisasi (% populasi kota) vs kapasitas infrastruktur kota (per penduduk)",
            "pemilik": "Kementerian PUPR & Pemerintah Daerah",
        },
        {
            "aksi": "Siapkan transisi tenaga kerja dari pertanian ke sektor produktif",
            "langkah": [
                "Ukur pergeseran tenaga kerja pertanian ke industri/jasa yang tercermin dalam tren urbanisasi 1960–2025.",
                "Rancang program pelatihan ulang (upskilling) dengan kurikulum berbasis kebutuhan sektor kota yang tumbuh.",
                "Buka akses kredit mikro/UMKM bagi pekerja yang berpindah sektor.",
            ],
            "metrik": "Porsi tenaga kerja sektor produktif (%) & tingkat serapan pelatihan ulang",
            "pemilik": "Kementerian Ketenagakerjaan & Kementerian Koperasi/UMKM",
        },
        {
            "aksi": "Antisipasi kesenjangan kota-desa dalam arus urbanisasi",
            "langkah": [
                "Petakan indikator desa yang tertinggal relatif terhadap pertumbuhan kota pada seri 1960–2025.",
                "Alokasikan dana desa & konektivitas (jalan, internet) ke wilayah dengan kesenjangan terbesar.",
                "Tetapkan target pengurangan kesenjangan kota-desa yang diukur berkala.",
            ],
            "metrik": "Indeks kesenjangan kota-desa (pendapatan/infrastruktur) & rasio Gini antar-wilayah",
            "pemilik": "Kementerian Desa (Kemendes) & Bappenas",
        },
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
        {
            "aksi": "Pantau indikator sosial per daerah, bukan hanya rata-rata nasional",
            "langkah": [
                "Uraikan harapan hidup & penetrasi internet nasional (seri 1960–2025) menjadi potret per provinsi.",
                "Tandai wilayah yang tertinggal (mis. Papua, NTT) sebagai zona prioritas berbasis skor indikator.",
                "Rutin publikasikan dasbor ketimpangan sosial antar-daerah sebagai dasar alokasi.",
            ],
            "metrik": "Harapan hidup (tahun) & penetrasi internet (%) per provinsi vs rata-rata nasional",
            "pemilik": "BPS & Kementerian Kesehatan",
        },
        {
            "aksi": "Alokasikan investasi pendidikan & kesehatan ke wilayah terendah",
            "langkah": [
                "Petakan wilayah dengan indikator pendidikan & kesehatan terendah terhadap seri nasional 1960–2025.",
                "Geser porsi anggaran pendidikan/kesehatan ke wilayah peringkat bawah tiap siklus anggaran.",
                "Sambungkan dengan indikator lama sekolah & angka harapan hidup sebagai target hasil.",
            ],
            "metrik": "Angka harapan lama sekolah (tahun) & belanja kesehatan per kapita per wilayah",
            "pemilik": "Kementerian Pendidikan & Kementerian Kesehatan",
        },
        {
            "aksi": "Jadikan digitalisasi katalis pemerataan akses ke daerah 3T",
            "langkah": [
                "Kaitkan tren penetrasi internet 1960–2025 dengan kesenjangan akses di wilayah terdepan, terluar, tertinggal (3T).",
                "Prioritaskan pembangunan infrastruktur internet di wilayah 3T dengan target cakupan eksplisit.",
                "Hubungkan akses internet dengan layanan pendidikan/kesehatan daring untuk mengurangi jurang layanan.",
            ],
            "metrik": "Cakupan internet daerah 3T (%) & indeks pemerataan digital antar-wilayah",
            "pemilik": "Kementerian Kominfo & BAKTI",
        },
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
        {
            "aksi": "Gunakan korelasi sebagai hipotesis, bukan kesimpulan kebijakan",
            "langkah": [
                "Pilih pasangan indikator dengan koefisien korelasi Pearson terkuat dari matriks 17 indikator.",
                "Terjemahkan tiap korelasi kuat menjadi hipotesis kausal yang dapat diuji (eksperimen/kuasi-eksperimen).",
                "Tetapkan syarat lulus uji kausalitas sebelum korelasi dipakai sebagai dasar kebijakan.",
            ],
            "metrik": "Koefisien korelasi Pearson (r) & status validasi kausalitas per hipotesis",
            "pemilik": "Bappenas & unit riset kebijakan (BRIN)",
        },
        {
            "aksi": "Waspadai confounding pada tren yang naik bersama karena waktu",
            "langkah": [
                "Deteksi indikator yang naik serentak pada seri 1960–2025 (GDP, internet, harapan hidup) sebagai kandidat korelasi semu.",
                "Kendalikan efek tren waktu (detrending) sebelum menyimpulkan hubungan antar-indikator.",
                "Uji stabilitas korelasi pada sub-periode (era) untuk memisahkan hubungan nyata dari spurious.",
            ],
            "metrik": "Korelasi setelah detrending & stabilitas korelasi antar-era (r per periode)",
            "pemilik": "BPS & BRIN",
        },
        {
            "aksi": "Fokus pada hubungan yang kuat dan konsisten dengan teori ekonomi",
            "langkah": [
                "Saring pasangan indikator dengan korelasi kuat dari matriks Pearson antar-17 indikator.",
                "Uji kesesuaian tiap hubungan kuat dengan teori ekonomi sebelum diprioritaskan.",
                "Susun daftar pendek hubungan 'kuat + masuk akal' sebagai prioritas riset kausalitas.",
            ],
            "metrik": "Skor gabungan kekuatan korelasi (r) & kesesuaian teori (kuat/lemah)",
            "pemilik": "Bappenas",
        },
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
        {
            "aksi": "Sajikan proyeksi sebagai skenario, bukan ramalan pasti",
            "langkah": [
                "Jalankan model forecast 5 tahun (horizon) menjadi tiga skenario: optimis, basis, pesimis.",
                "Ikat rentang skenario pada variasi pertumbuhan historis 1960–2025 (termasuk 1998 & 2020).",
                "Laporkan setiap skenario beserta peluangnya, bukan satu angka tunggal.",
            ],
            "metrik": "Rentang GDP per kapita per skenario (US$) & selang kepercayaan",
            "pemilik": "Bappenas & Bank Indonesia",
        },
        {
            "aksi": "Batasi horizon proyeksi agar ketidakpastian tetap terkendali",
            "langkah": [
                "Potong forekast pada horizon di mana backtest MAPE masih di bawah ambang toleransi.",
                "Ukur kenaikan error (MAPE) seiring bertambahnya jarak proyeksi.",
                "Tetapkan aturan agar horizon maksimum dipublikasikan bersama level ketidakpastiannya.",
            ],
            "metrik": "Backtest MAPE (%) per horizon & R² model forecast",
            "pemilik": "BRIN & Bank Indonesia",
        },
        {
            "aksi": "Sertakan asumsi eksplisit & batas kepercayaan pada setiap proyeksi",
            "langkah": [
                "Daftarkan asumsi kunci model (inflasi, investasi, populasi) secara terbuka.",
                "Waspadai inflasi yang volatil dan uji ulang model terhadap periode inflasi tinggi 1960–2025.",
                "Sajikan setiap proyeksi bersama rentang kepercayaan, jangan angka tanpa rentang.",
            ],
            "metrik": "Jumlah asumsi terdokumentasi & lebar rentang kepercayaan proyeksi",
            "pemilik": "BPS & Bank Indonesia",
        },
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
        {
            "aksi": "Pelajari faktor pendorong era pertumbuhan tinggi tanpa mereplikasinya",
            "langkah": [
                "Bedah era Orde Baru (1967–1997) & boom komoditas (2000–2013) pada seri 1960–2025 untuk faktor pendorongnya.",
                "Pisahkan faktor yang masih relevan dari yang bergantung konteks era (kini sudah berubah).",
                "Terjemahkan faktor relevan menjadi rekomendasi kebijakan kontemporer, bukan penyalinan.",
            ],
            "metrik": "Kontribusi faktor pendorong kunci terhadap pertumbuhan per era (%)",
            "pemilik": "Bappenas & BRIN",
        },
        {
            "aksi": "Identifikasi kerentanan struktural dari era krisis (1998 & COVID-19)",
            "langkah": [
                "Uraikan karakter era Krisis Asia (1998–1999) & COVID-19 (2020–2021) dari seri 1960–2025.",
                "Daftarkan kerentanan struktural yang muncul berulang di kedua krisis.",
                "Bentuk program mitigasi khusus untuk kerentanan yang berulang tersebut.",
            ],
            "metrik": "Daftar kerentanan struktural berulang & kedalaman kontraksi per krisis (%)",
            "pemilik": "Kementerian Keuangan & Bappenas",
        },
        {
            "aksi": "Tetapkan target era saat ini berbasis realitas fondasi makro",
            "langkah": [
                "Upayakan benchmarking era Perlambatan (2014–2019) & Pemulihan (2022–2025) terhadap era sebelumnya dalam seri 1960–2025.",
                "Susun target pertumbuhan periode ini dari fondasi makro nyata, bukan nostalgia era REPELITA.",
                "Selaraskan target dengan tantangan baru: digitalisasi, iklim, dan demografi.",
            ],
            "metrik": "Target pertumbuhan GDP (%) vs realisasi era saat ini & baseline fondasi makro",
            "pemilik": "Bappenas & Kementerian Keuangan",
        },
    ],
    risiko=(
        "Mengejar pertumbuhan era lama tanpa memahami perbedaan konteks = target "
        "takrealistis. Kebijakan berbasis nostalgia bisa mengabaikan tantangan "
        "baru (digitalisasi, iklim, demografi)."),
    tingkat="sedang",
)


# --------------------------------------------------------------------------
# Chart ECharts (v2) — insight & rekomendasi.
# --------------------------------------------------------------------------

register(
    "echarts_parallel",
    kesimpulan=(
        "Parallel coordinates membandingkan profil 8 indikator antar-ERA ekonomi "
        "(dinormalisasi 0–1). Terlihat pergeseran struktur: dari era GDP per "
        "kapita rendah + populasi besar + internet nol, menuju era IPM tinggi + "
        "internet tinggi + CO2 naik. Ini menegaskan Indonesia bergerak dari "
        "ekonomi agraris ke ekonomi modern — tetapi dengan konsekuensi emisi."),
    rekomendasi=[
        {
            "aksi": "Baca pergeseran antar-era sebagai konteks trade-off kebijakan",
            "langkah": [
                "Bandingkan profil 8 indikator ternormalisasi antar-era pada parallel coordinates (Orde Lama sampai Pemulihan 2022–2025).",
                "Tandai sumbu yang menunjukkan trade-off jelas (mis. GDP naik vs CO2 naik).",
                "Rumuskan kebijakan yang mengelola trade-off tersebut per era target.",
            ],
            "metrik": "Posisi ternormalisasi 8 indikator per era (0–1) & besarnya trade-off antar-sumbu",
            "pemilik": "Bappenas & Kementerian Lingkungan Hidup",
        },
        {
            "aksi": "Prioritaskan sumbu yang stagnan atau memburuk (Gini, pengangguran)",
            "langkah": [
                "Identifikasi sumbu indikator yang datar/memburuk di seluruh era pada profil parallel coordinates.",
                "Kaitkan dengan seri 1960–2025 untuk memastikan stagnasi bersifat struktural, bukan kebetulan.",
                "Tetapkan target perbaikan eksplisit untuk indikator stagnan sebagai prioritas kebijakan.",
            ],
            "metrik": "Gini & tingkat pengangguran (%) per era vs target perbaikan",
            "pemilik": "BPS & Kementerian Ketenagakerjaan",
        },
        {
            "aksi": "Hindari membandingkan era krisis langsung dengan era normal",
            "langkah": [
                "Tandai profil era krisis (Krisis Asia 1998–1999, COVID-19 2020–2021) pada parallel coordinates.",
                "Selalu sertakan konteks guncangan sebelum membandingkan dengan era normal (Orde Baru, boom komoditas).",
                "Normalisasi perbandingan terhadap kondisi makro masing-masing era.",
            ],
            "metrik": "Selisih indikator era krisis vs era normal setelah penyesuaian konteks",
            "pemilik": "Bappenas & BRIN",
        },
    ],
    risiko=(
        "Membaca tren jangka panjang tanpa memisahkan guncangan (krisis) "
        "berisiko menyimpulkan 'perlambatan struktural' padahal itu efek sementara. "
        "Sebaliknya, mengabaikan stagnasi sosial bisa menutupi masalah nyata."),
    tingkat="sedang",
)

register(
    "echarts_boxplot",
    kesimpulan=(
        "Boxplot indikator per dekade menunjukkan STABILITAS: kotak sempit = "
        "pertumbuhan mulus (mis. GDP growth era 2000–2010an), kotak tinggi = "
        "gejolak besar (era 1960an, krisis 1990an). Pencilan menandai kejadian "
        "ekstrem — mis. kontraksi 1998 atau COVID 2020."),
    rekomendasi=[
        {
            "aksi": "Gunakan sebaran (bukan rata-rata) untuk menilai risiko indikator",
            "langkah": [
                "Baca lebar kotak & jangkauan boxplot indikator per dekade pada seri 1960–2025.",
                "Tetapkan penyangga kebijakan lebih besar untuk dekade bergejolak (kotak tinggi).",
                "Sesuaikan alokasi cadangan berdasarkan lebar sebaran, bukan hanya rata-rata.",
            ],
            "metrik": "Lebar sebaran (IQR) indikator per dekade & ukuran penyangga kebijakan",
            "pemilik": "Kementerian Keuangan & Bappenas",
        },
        {
            "aksi": "Selidiki pencilan sebagai pelajaran kesiapan krisis",
            "langkah": [
                "Identifikasi pencilan ekstrem pada boxplot, khususnya kontraksi 1998 dan COVID-19 2020.",
                "Uraikan penyebab tiap pencilan dari seri pertumbuhan 1960–2025.",
                "Ubah temuan menjadi skenario kesiapan menghadapi guncangan berikutnya.",
            ],
            "metrik": "Frekuensi & magnitudo pencilan ekstrem per dekade (% deviasi dari median)",
            "pemilik": "BRIN & Bappenas",
        },
        {
            "aksi": "Jangkar perencanaan jangka panjang pada dekade stabil",
            "langkah": [
                "Pisahkan dekade stabil (kotak sempit, mis. 2000–2010an) dari dekade bergejolak pada boxplot.",
                "Tetapkan baseline perencanaan dari dekade stabil, bukan rata-rata seluruh periode 1960–2025.",
                "Uji ulang rencana terhadap skenario dekade ekstrem (1960an, 1990an).",
            ],
            "metrik": "Baseline indikator dari dekade stabil vs keberlangsungan rencana di bawah skenario ekstrem",
            "pemilik": "Bappenas & Kementerian Keuangan",
        },
    ],
    risiko=(
        "Mengambil rata-rata lintas dekade mencampur era stabil & krisis, "
        "menghasilkan target yang tak realistis. Perencanaan berbasis angka itu "
        "bisa gagal saat kondisi ekstrem kembali."),
    tingkat="sedang",
)
