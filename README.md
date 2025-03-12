# 🐍SUBMISSION ANALISIS DATA DENGAN PYTHON🐍

## 💻 Tampilan Dashboard
![Demo GIF](https://github.com/tianiayu/kumpulangif/blob/53998decabbe14648de4a65b8cdfdad1f427851f/Submission%201.gif)

## 📌 Deskripsi
Proyek ini berisi kode untuk membuat Bike Sharing Dashboard menggunakan Streamlit 👑

## 🎯 Tujuan dan Teknik Analisis
1. Analisis jumlah peminjaman berdasarkan jam untuk melihat jam-jam sibuk:
<br>*Mengidentifikasi jam-jam sibuk
<br>*Menganalisis pola penggunaan harian
2. Perbandingan registered vs casual sepanjang tahun:
<br>*Menganalisis tren jumlah peminjaman oleh pengguna registered dan casual sepanjang tahun

## 📂 Struktur Data
Berikut adalah struktur file dalam proyek ini:
.<br>/dashboard       = Berisi file dataset yang sudah di cleaning serta kode dashboar.py untuk visualisasi data
.<br>/data            = Berisi dataset mentah bike-sharing (hour.csv dan day.csv)
.<br>README.md        = Berisi domumentasi proyek 
.<br>notebook.ipynb   = Berisi File Jupyter Notebook
.<br>requirements.txt = Berisi daftar pustaka python yang dibutuhkan untuk menjalankan project ini
.<br>url.txt          = berisi link hasil dashboard yang telah di deploy

## 📟 Setup Environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
pip install pipreqs
pip install streamlit
```

## 🚀 Cara Menjalankan
Jalankan Streamlit masuk ke directori proyek dengan perintah berikut:
```
streamlit run submission1.py
```
Atau bisa mengakses link berikut https://submission-1.streamlit.app/
