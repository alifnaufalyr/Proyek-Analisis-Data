import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv('day.csv')  # Sesuaikan dengan nama file dataset yang digunakan

# Title of the Dashboard
st.title("Bike Sharing Data Analysis")

# Sidebar Options
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim:", df['season'].unique())
workingday_filter = st.sidebar.selectbox("Pilih Hari Kerja (0: Libur, 1: Hari Kerja):", df['workingday'].unique())

# Apply Filters
df_filtered = df[(df['season'] == season_filter) & (df['workingday'] == workingday_filter)]

# Display Data
st.subheader("Dataset Sample")
st.write(df_filtered.head())

# Visualization: Jumlah Peminjaman Sepeda Berdasarkan Musim
st.subheader("Jumlah Peminjaman Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x=df['season'], y=df['cnt'], palette='coolwarm', ax=ax)
plt.xlabel("Musim")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Visualization: Pengaruh Hari Kerja terhadap Peminjaman Sepeda
st.subheader("Pengaruh Hari Kerja terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x=df['workingday'], y=df['cnt'], palette='viridis', ax=ax)
plt.xlabel("Hari Kerja (0: Libur, 1: Hari Kerja)")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Conclusion
st.subheader("Kesimpulan")
st.markdown("- Jumlah peminjaman sepeda lebih tinggi pada musim tertentu.\n- Hari kerja memiliki pengaruh terhadap tren peminjaman sepeda.")
