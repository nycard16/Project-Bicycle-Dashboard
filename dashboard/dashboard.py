import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat dataset gabungan
all_data = pd.read_csv('/all_data_clean.csv')

# Judul dashboard
st.title('Dashboard Analisis Penyewaan Sepeda')

# Sidebar untuk navigasi
st.sidebar.title('Navigasi')
options = st.sidebar.radio('Pilih analisis:', ['Analisis Harian', 'Analisis Per Jam'])

if options == 'Analisis Harian':
    st.header('Analisis Data Harian')

    # Menampilkan dataset
    st.subheader('Dataset')
    st.write(all_data[['instant_day', 'dteday', 'season_day', 'yr_day', 'mnth_day', 'holiday_day', 'weekday_day', 'workingday_day', 'weathersit_day', 'temp_day', 'atemp_day', 'hum_day', 'windspeed_day', 'casual_day', 'registered_day', 'cnt_day']].head())

    # Keterangan dataset
    st.markdown("""
    **Keterangan Kolom:**
    - **instant_day**: Indeks rekaman
    - **dteday**: Tanggal
    - **season_day**: Musim (1: musim dingin, 2: musim semi, 3: musim panas, 4: musim gugur)
    - **yr_day**: Tahun (0: 2011, 1: 2012)
    - **mnth_day**: Bulan (1 hingga 12)
    - **holiday_day**: Apakah hari libur (0: Tidak, 1: Ya)
    - **weekday_day**: Hari dalam seminggu (0: Minggu hingga 6: Sabtu)
    - **workingday_day**: Apakah hari kerja (0: Tidak, 1: Ya)
    - **weathersit_day**: Situasi cuaca (1: Cerah, 2: Berkabut, 3: Hujan/Salju ringan, 4: Hujan/Salju lebat)
    - **temp_day**: Suhu normalisasi dalam Celsius
    - **atemp_day**: Suhu terasa normalisasi dalam Celsius
    - **hum_day**: Kelembaban normalisasi
    - **windspeed_day**: Kecepatan angin normalisasi
    - **casual_day**: Jumlah pengguna kasual
    - **registered_day**: Jumlah pengguna terdaftar
    - **cnt_day**: Total jumlah penyewaan sepeda (kasual + terdaftar)
    """)

    # Plot total penyewaan berdasarkan musim
    st.subheader('Total Penyewaan Berdasarkan Musim')
    st.markdown("Grafik ini menunjukkan total penyewaan sepeda berdasarkan musim.")
    fig, ax = plt.subplots()
    sns.barplot(x='season_day', y='cnt_day', data=all_data, ax=ax)
    ax.set_xlabel('Musim')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Berdasarkan Musim')
    st.pyplot(fig)
    st.markdown("""
    **Kesimpulan:**
    - Musim panas dan musim gugur memiliki jumlah penyewaan sepeda tertinggi.
    - Musim dingin memiliki jumlah penyewaan sepeda terendah.
    """)

    # Plot total penyewaan berdasarkan bulan
    st.subheader('Total Penyewaan Berdasarkan Bulan')
    st.markdown("Grafik ini menunjukkan total penyewaan sepeda berdasarkan bulan.")
    fig, ax = plt.subplots()
    sns.lineplot(x='mnth_day', y='cnt_day', data=all_data, ax=ax)
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Berdasarkan Bulan')
    st.pyplot(fig)
    st.markdown("""
    **Kesimpulan:**
    - Penyewaan sepeda cenderung meningkat selama bulan-bulan musim panas (Juni, Juli, Agustus).
    - Penyewaan sepeda menurun selama bulan-bulan musim dingin (Desember, Januari, Februari).
    """)

    # Plot total penyewaan berdasarkan situasi cuaca
    st.subheader('Total Penyewaan Berdasarkan Situasi Cuaca')
    st.markdown("Grafik ini menunjukkan total penyewaan sepeda berdasarkan situasi cuaca.")
    fig, ax = plt.subplots()
    sns.barplot(x='weathersit_day', y='cnt_day', data=all_data, ax=ax)
    ax.set_xlabel('Situasi Cuaca')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Berdasarkan Situasi Cuaca')
    st.pyplot(fig)
    st.markdown("""
    **Kesimpulan:**
    - Cuaca cerah memiliki jumlah penyewaan sepeda tertinggi.
    - Cuaca hujan atau salju lebat memiliki jumlah penyewaan sepeda terendah.
    """)

elif options == 'Analisis Per Jam':
    st.header('Analisis Data Per Jam')

    # Menampilkan dataset
    st.subheader('Dataset')
    st.write(all_data[['instant_hour', 'dteday', 'season_hour', 'yr_hour', 'mnth_hour', 'hr', 'holiday_hour', 'weekday_hour', 'workingday_hour', 'weathersit_hour', 'temp_hour', 'atemp_hour', 'hum_hour', 'windspeed_hour', 'casual_hour', 'registered_hour', 'cnt_hour']].head())

    # Keterangan dataset
    st.markdown("""
    **Keterangan Kolom:**
    - **instant_hour**: Indeks rekaman
    - **dteday**: Tanggal
    - **season_hour**: Musim (1: musim dingin, 2: musim semi, 3: musim panas, 4: musim gugur)
    - **yr_hour**: Tahun (0: 2011, 1: 2012)
    - **mnth_hour**: Bulan (1 hingga 12)
    - **hr**: Jam (0 hingga 23)
    - **holiday_hour**: Apakah hari libur (0: Tidak, 1: Ya)
    - **weekday_hour**: Hari dalam seminggu (0: Minggu hingga 6: Sabtu)
    - **workingday_hour**: Apakah hari kerja (0: Tidak, 1: Ya)
    - **weathersit_hour**: Situasi cuaca (1: Cerah, 2: Berkabut, 3: Hujan/Salju ringan, 4: Hujan/Salju lebat)
    - **temp_hour**: Suhu normalisasi dalam Celsius
    - **atemp_hour**: Suhu terasa normalisasi dalam Celsius
    - **hum_hour**: Kelembaban normalisasi
    - **windspeed_hour**: Kecepatan angin normalisasi
    - **casual_hour**: Jumlah pengguna kasual
    - **registered_hour**: Jumlah pengguna terdaftar
    - **cnt_hour**: Total jumlah penyewaan sepeda (kasual + terdaftar)
    """)

    # Plot total penyewaan berdasarkan jam
    st.subheader('Total Penyewaan Berdasarkan Jam')
    st.markdown("Grafik ini menunjukkan total penyewaan sepeda berdasarkan jam.")
    fig, ax = plt.subplots()
    sns.lineplot(x='hr', y='cnt_hour', data=all_data, ax=ax)
    ax.set_xlabel('Jam')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Berdasarkan Jam')
    st.pyplot(fig)
    st.markdown("""
    **Kesimpulan:**
    - Penyewaan sepeda mencapai puncaknya pada jam sibuk pagi (sekitar jam 8) dan sore (sekitar jam 17-18).
    - Penyewaan sepeda paling rendah pada dini hari (jam 2-4).
    """)

    # Plot total penyewaan berdasarkan hari kerja
    st.subheader('Total Penyewaan Berdasarkan Hari Kerja')
    st.markdown("Grafik ini menunjukkan total penyewaan sepeda berdasarkan hari kerja.")
    fig, ax = plt.subplots()
    sns.barplot(x='weekday_hour', y='cnt_hour', data=all_data, ax=ax)
    ax.set_xlabel('Hari Kerja')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Berdasarkan Hari Kerja')
    st.pyplot(fig)
    st.markdown("""
    **Kesimpulan:**
    - Penyewaan sepeda lebih tinggi pada hari kerja dibandingkan dengan akhir pekan.
    - Penyewaan sepeda paling rendah pada hari Minggu.
    """)

    # Plot total penyewaan berdasarkan situasi cuaca
    st.subheader('Total Penyewaan Berdasarkan Situasi Cuaca')
    st.markdown("Grafik ini menunjukkan total penyewaan sepeda berdasarkan situasi cuaca.")
    fig, ax = plt.subplots()
    sns.barplot(x='weathersit_hour', y='cnt_hour', data=all_data, ax=ax)
    ax.set_xlabel('Situasi Cuaca')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Berdasarkan Situasi Cuaca')
    st.pyplot(fig)
    st.markdown("""
    **Kesimpulan:**
    - Cuaca cerah memiliki jumlah penyewaan sepeda tertinggi.
    """)
