import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sidebar gambar dan judul
st.sidebar.image("download.png", use_column_width=True)
st.sidebar.title("Bike Sharing Dashboard")
st.sidebar.markdown("### Analisis Penggunaan Sepeda")

# Membaca data CSV day dan hour
day_data = pd.read_csv("https://raw.githubusercontent.com/devacantika/bike/refs/heads/main/dataset/day.csv")
hour_data = pd.read_csv("https://raw.githubusercontent.com/devacantika/bike/refs/heads/main/dataset/hour.csv")

# Ubah kolom 'dteday' ke format tanggal
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

# Sidebar rentang waktu (opsional untuk filter data)
date_range = st.sidebar.date_input("Pilih Rentang Waktu", [])

# Judul dashboard
st.title("Dashboard Penggunaan Sepeda")

# --------------------- Visualisasi 1: Pengaruh Musim terhadap Penggunaan Sepeda ---------------------
st.subheader("Pengaruh Musim terhadap Jumlah Pengguna Sepeda")

season_group = day_data.groupby('season')['cnt'].mean().reset_index()

fig1, ax1 = plt.subplots()
sns.barplot(x='season', y='cnt', data=season_group, ax=ax1)
ax1.set_title('Penggunaan Sepeda Berdasarkan Musim')
ax1.set_xlabel('Musim')
ax1.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
st.pyplot(fig1)

# --------------------- Visualisasi 2: Penggunaan Sepeda Berdasarkan Jam ---------------------
st.subheader("Penggunaan Sepeda Berdasarkan Jam dalam Sehari")

hour_group = hour_data.groupby('hr')['cnt'].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.lineplot(x='hr', y='cnt', data=hour_group, ax=ax2)
ax2.set_title('Penggunaan Sepeda Berdasarkan Jam dalam Sehari')
ax2.set_xlabel('Jam')
ax2.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
st.pyplot(fig2)

# --------------------- Visualisasi 3: Penggunaan Sepeda oleh Casual vs Registered ---------------------
st.subheader("Penggunaan Sepeda oleh Pengguna Casual dan Terdaftar")

user_type_group = day_data[['casual', 'registered']].mean()

fig3, ax3 = plt.subplots()
user_type_group.plot(kind='bar', ax=ax3, color=['skyblue', 'salmon'])
ax3.set_title('Rata-rata Penggunaan Sepeda: Casual vs Registered')
ax3.set_xlabel('Tipe Pengguna')
ax3.set_ylabel('Rata-rata Jumlah Pengguna')
st.pyplot(fig3)

# Insight section
st.markdown("### Insight:")
st.markdown("- **Pengaruh Musim**: Penggunaan sepeda paling tinggi selama musim panas, dan paling rendah selama musim dingin.")
st.markdown("- **Penggunaan Berdasarkan Jam**: Penggunaan sepeda cenderung meningkat selama jam sibuk pagi dan sore.")
st.markdown("- **Pengguna Casual vs Registered**: Pengguna terdaftar menggunakan sepeda lebih sering dibandingkan pengguna kasual, terutama pada hari kerja.")
