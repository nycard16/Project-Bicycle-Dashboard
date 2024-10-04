import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

# Load data
data = pd.read_csv(r'dashboard/all_data_clean.csv')

# Title and Logo
st.title('Dashboard Penggunaan Bike Sharing')
st.sidebar.image(r'dashboard/logo.png', use_column_width=True)

# Sidebar Variations
st.sidebar.header('Navigasi')
with st.sidebar.expander("Analisis"):
    page = st.sidebar.radio("Pilih Analisis:", ["Ringkasan Data", "Pertanyaan Bisnis", "Jumlah Pengguna per Jam", "Pengaruh Cuaca terhadap Penggunaan Sepeda", "Penggunaan Sepeda Berdasarkan Kondisi Kerja", "Persentase Penggunaan Sepeda pada Hari Kerja dan Hari Libur", "Persentase Rata-rata Jumlah Pengguna Sepeda Berdasarkan Musim", "Tren Pengguna Sepeda"])

# Background
st.header('Latar Belakang')
st.markdown("""
Sistem Bike Sharing adalah generasi baru dari penyewaan sepeda tradisional, di mana seluruh proses mulai dari keanggotaan,
penyewaan, hingga pengembalian telah menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari lokasi
tertentu dan mengembalikannya di lokasi lain. Saat ini, terdapat lebih dari 500 program Bike Sharing di seluruh dunia 
yang terdiri dari lebih dari 500 ribu sepeda. Sistem ini sangat diminati karena perannya yang penting dalam masalah lalu lintas, lingkungan, dan kesehatan.

Selain aplikasinya yang menarik di dunia nyata, karakteristik data yang dihasilkan oleh sistem Bike Sharing juga menarik untuk penelitian.
Berbeda dengan layanan transportasi lainnya seperti bus atau kereta bawah tanah, durasi perjalanan, lokasi keberangkatan, dan lokasi kedatangan dicatat secara eksplisit dalam sistem ini. 
Fitur ini mengubah sistem berbagi sepeda menjadi jaringan sensor virtual yang dapat digunakan untuk memantau mobilitas di kota.
Oleh karena itu, diharapkan bahwa sebagian besar peristiwa penting di kota dapat terdeteksi melalui pemantauan data ini.
""")

# Data Set
st.header('Data Set')
st.markdown("""
Proses penyewaan sepeda sangat dipengaruhi oleh faktor lingkungan dan musiman. Misalnya, kondisi cuaca, curah hujan, hari dalam seminggu, musim, jam dalam sehari, dll.
dapat memengaruhi perilaku penyewaan. Data inti berkaitan dengan catatan historis dua tahun untuk tahun 2011 dan 2012 dari sistem Capital Bikeshare, Washington D.C., AS 
""")

# Conditional Display
if page == "Ringkasan Data":
    st.header('Ringkasan Data')
    st.write(data[['dteday', 'season_hour', 'yr_hour', 'mnth_hour', 'hr', 'holiday_hour', 'weekday_hour', 'workingday_hour', 'weathersit_hour', 'temp_hour', 'atemp_hour', 'hum_hour', 'windspeed_hour', 'casual_hour', 'registered_hour', 'cnt_hour']].describe(include='all'))
    st.markdown("""
    **Keterangan Data:**
    - `instant_hour`: ID unik untuk setiap baris data per jam.
    - `dteday`: Tanggal data.
    - `season_hour`: Musim (1: Musim Semi, 2: Musim Panas, 3: Musim Gugur, 4: Musim Dingin).
    - `yr_hour`: Tahun (0: 2011, 1: 2012).
    - `mnth_hour`: Bulan (1 sampai 12).
    - `hr`: Jam (0 sampai 23).
    - `holiday_hour`: Apakah hari libur (0: Bukan, 1: Ya).
    - `weekday_hour`: Hari dalam minggu (0: Minggu, 1: Senin, ..., 6: Sabtu).
    - `workingday_hour`: Apakah hari kerja (0: Bukan, 1: Ya).
    - `weathersit_hour`: Kondisi cuaca (1: Cerah, 2: Berawan, 3: Hujan ringan, 4: Hujan lebat).
    - `temp_hour`: Suhu normalisasi.
    - `atemp_hour`: Suhu terasa normalisasi.
    - `hum_hour`: Kelembaban normalisasi.
    - `windspeed_hour`: Kecepatan angin normalisasi.
    - `casual_hour`: Jumlah pengguna kasual.
    - `registered_hour`: Jumlah pengguna terdaftar.
    - `cnt_hour`: Jumlah total pengguna.
    """)
    st.session_state.page = page

elif page == "Pertanyaan Bisnis":
    st.header('Pertanyaan Bisnis')
    st.markdown("""
    1. **Bagaimana pengaruh cuaca terhadap penggunaan Bike Sharing di Washington D.C.?**
    2. **Apakah ada perbedaan penggunaan Bike Sharing antara hari kerja dan hari libur?**
    3. **Berapa persentase penggunaan Bike Sharing pada hari kerja dan hari libur?**
    4. **Berapa persentase rata-rata jumlah pengguna sepeda berdasarkan musim?**
    """)
    st.session_state.page = page

elif page == "Jumlah Pengguna per Jam":
    st.header('Jumlah Pengguna per Jam')
    st.markdown("Grafik ini menunjukkan jumlah pengguna kasual dan terdaftar per jam. Terlihat bahwa jumlah pengguna meningkat pada jam-jam sibuk pagi dan sore hari.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=data, x='hr', y='cnt_hour', hue='weekday_hour', ax=ax)
    ax.set_title('Jumlah Pengguna per Jam')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Pengguna')
    st.pyplot(fig)
    st.markdown("**Kesimpulan**: Jumlah pengguna Bike Sharing cenderung meningkat pada jam-jam sibuk pagi dan sore hari, yang menunjukkan bahwa banyak orang menggunakan sepeda untuk perjalanan ke dan dari tempat kerja atau sekolah.")
    st.session_state.page = page

elif page == "Pengaruh Cuaca terhadap Penggunaan Sepeda":
    st.header('Pengaruh Cuaca terhadap Penggunaan Sepeda')
    st.markdown("Grafik ini menunjukkan pengaruh kondisi cuaca terhadap jumlah pengguna. Terlihat bahwa cuaca yang lebih baik cenderung meningkatkan jumlah pengguna.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=data, x='weathersit_hour', y='cnt_hour', ax=ax)
    ax.set_title('Pengaruh Cuaca terhadap Penggunaan Sepeda')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Pengguna')
    ax.set_xticklabels(['Cerah', 'Berawan', 'Hujan ringan', 'Hujan lebat'])
    st.pyplot(fig)
    st.markdown("**Kesimpulan**: Cuaca yang lebih baik cenderung meningkatkan jumlah pengguna Bike Sharing. Pengguna lebih banyak saat cuaca cerah dibandingkan saat cuaca buruk.")
    st.session_state.page = page

elif page == "Penggunaan Sepeda Berdasarkan Kondisi Kerja":
    st.header('Penggunaan Sepeda Berdasarkan Kondisi Kerja')
    st.markdown("Grafik ini menunjukkan perbedaan jumlah pengguna pada hari kerja, akhir pekan, dan hari libur. Terlihat bahwa jumlah pengguna lebih tinggi pada akhir pekan dan hari libur.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=data, x='workingday_hour', y='cnt_hour', ax=ax)
    ax.set_title('Penggunaan Sepeda Berdasarkan Kondisi Kerja')
    ax.set_xlabel('Kondisi Kerja (0: Libur, 1: Kerja)')
    ax.set_ylabel('Jumlah Pengguna')
    st.pyplot(fig)
    st.markdown("**Kesimpulan**: Jumlah pengguna Bike Sharing lebih tinggi pada akhir pekan dan hari libur dibandingkan dengan hari kerja.")
    st.session_state.page = page

elif page == "Persentase Penggunaan Sepeda pada Hari Kerja dan Hari Libur":
    st.header('Persentase Penggunaan Sepeda pada Hari Kerja dan Hari Libur')
    st.markdown("Grafik ini menunjukkan persentase penggunaan sepeda pada hari kerja dan hari libur.")
    fig, ax = plt.subplots(figsize=(10, 6))
    labels = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
    plt.pie(data['weekday_hour'].value_counts(), labels=labels, autopct='%1.1f%%')
    plt.title('Persentase Penggunaan Sepeda pada Hari Kerja dan Hari Libur')
    st.pyplot(fig)
    st.markdown("**Kesimpulan**: Persentase penggunaan sepeda pada hari kerja dan hari libur terbagi rata antara 7 kategori (Minggu sampai Sabtu), dengan masing-masing kategori memiliki persentase penggunaan yang hampir sama (sekitar 14%).")
    st.session_state.page = page

elif page == "Persentase Rata-rata Jumlah Pengguna Sepeda Berdasarkan Musim":
    st.header('Persentase Rata-rata Jumlah Pengguna Sepeda Berdasarkan Musim')
    st.markdown("Grafik ini menunjukkan persentase rata-rata jumlah pengguna sepeda berdasarkan musim.")
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.pie(data.groupby('season_hour')['cnt_hour'].mean().values, labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'], autopct='%1.1f%%')
    plt.title('Persentase Rata-rata Jumlah Pengguna Sepeda Berdasarkan Musim')
    st.pyplot(fig)
    st.markdown("**Kesimpulan**: Persentase rata-rata jumlah pengguna sepeda berdasarkan musim adalah sekitar 14% untuk musim semi, 27% untuk musim panas, 31% untuk musim gugur, dan 26% untuk musim dingin.")
    st.session_state.page = page

elif page == "Tren Pengguna Sepeda":
    st.header('Tren Pengguna Sepeda')
    st.markdown("Grafik ini menunjukkan tren jumlah pengguna dari waktu ke waktu. Terlihat adanya peningkatan jumlah pengguna pada bulan-bulan tertentu.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=data, x='dteday', y='cnt_hour', ax=ax)
    ax.set_title('Tren Pengguna Sepeda dari Waktu ke Waktu')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Pengguna')
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    st.pyplot(fig)
    st.markdown("**Kesimpulan**: Tren jumlah pengguna Bike Sharing menunjukkan adanya peningkatan pada bulan-bulan tertentu, yang mungkin terkait dengan kondisi cuaca yang lebih baik atau acara-acara khusus di kota.")
    st.session_state.page = page
