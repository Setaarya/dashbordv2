import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned datasets
day_df = pd.read_csv(r'/data/main_data.csv')

# Convert 'dteday' to datetime for filtering
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Menambahkan logo di sidebar
logo_path = "/dashboard/pngaaa.com-5084798.png"  # Ganti dengan jalur logo Anda
st.sidebar.image(logo_path, use_column_width=True)

st.title("Dashboard Analisis Penyewaan Sepeda")

# Sidebar for navigation
st.sidebar.title("Navigasi")

# Rentang tanggal input dari pengguna
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

date_range = st.sidebar.date_input("Pilih Rentang Tanggal", 
                                   value=[min_date, max_date],
                                   min_value=min_date,
                                   max_value=max_date)

# Filter data berdasarkan rentang tanggal yang dipilih
filtered_df = day_df[(day_df['dteday'] >= pd.to_datetime(date_range[0])) & 
                     (day_df['dteday'] <= pd.to_datetime(date_range[1]))]

# Menampilkan sumber data di sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("**Sumber Data:** [Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)")

# Visualisasi 1: Perbandingan Sewa Sepeda Setiap Hari
st.subheader("Perbandingan Penyewa Sepeda Setiap Hari")
plt.figure(figsize=(10, 6))
sns.barplot(x='weekday', y='cnt', data=filtered_df, 
            order=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], 
            errorbar=None)
plt.title('Perbandingan Penyewa Sepeda Setiap Hari')
plt.xlabel('Hari')
plt.ylabel('Jumlah Penyewa Sepeda')
st.pyplot(plt)

# Visualisasi 2: Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=filtered_df, errorbar=None)
plt.title('Jumlah Penyewa Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewa Sepeda')
st.pyplot(plt)

# Visualisasi 3: Sewa Sepeda Berdasarkan Jenis Hari
st.subheader("Sewa Sepeda Berdasarkan Jenis Hari")
plt.figure(figsize=(10, 6))
sns.pointplot(data=filtered_df, x='mnth', y='cnt', hue='workingday', 
              order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
                     'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
plt.title('Jumlah Penyewa Sepeda berdasarkan Jenis Hari')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewa Sepeda')
st.pyplot(plt)

# Visualisasi 4: Sewa Sepeda Berdasarkan Musim
st.subheader("Sewa Sepeda Berdasarkan Musim")
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=filtered_df, errorbar=None)
plt.title('Jumlah Penyewa Sepeda berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewa Sepeda')
st.pyplot(plt)

# Visualisasi 5: Jumlah Penyewa Sepeda Tiap Bulan
st.subheader("Jumlah Penyewa Sepeda Tiap Bulan")
plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_df, x='mnth', y='cnt', 
            order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
                   'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
plt.title('Penyewa Sepeda Setiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewa Sepeda')
st.pyplot(plt)

# Visualisasi 6: Tren Penyewaan Sepeda Tiap Bulan
st.subheader("Tren Penyewaan Sepeda Tiap Bulan")
plt.figure(figsize=(10, 6))
sns.pointplot(data=filtered_df, x='mnth', y='cnt', hue='yr', 
              order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
                     'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], errorbar=None)
plt.title('Tren Penyewa Sepeda')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewa Sepeda')
st.pyplot(plt)
