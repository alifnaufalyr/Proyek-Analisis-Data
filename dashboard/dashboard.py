import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("day.csv")

# Streamlit App
st.title("Dashboard Analisis Data Bike Sharing")
st.markdown("---")

# Sidebar for filtering
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", df["season"].unique())
filtered_df = df[df["season"] == selected_season]

# Histogram distribusi jumlah peminjaman sepeda
st.subheader("Distribusi Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df["cnt"], bins=30, kde=True, color="blue", ax=ax)
plt.xlabel("Jumlah Peminjaman Sepeda")
plt.ylabel("Frekuensi")
st.pyplot(fig)

# Boxplot perbandingan peminjaman sepeda berdasarkan musim
st.subheader("Perbandingan Jumlah Peminjaman Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x=df["season"], y=df["cnt"], palette="coolwarm", ax=ax)
plt.xlabel("Musim")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# Boxplot perbandingan peminjaman sepeda pada hari kerja vs hari libur
st.subheader("Perbandingan Peminjaman Sepeda: Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x=df["workingday"], y=df["cnt"], palette="viridis", ax=ax)
plt.xlabel("Hari Kerja (0: Libur, 1: Hari Kerja)")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

st.markdown("---")
st.write("Dashboard ini menampilkan analisis peminjaman sepeda berdasarkan berbagai faktor seperti musim dan hari kerja.")
