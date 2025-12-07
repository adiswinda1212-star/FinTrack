import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

@st.cache_data
def load_data():
    df = pd.read_csv("data/transactions.csv", parse_dates=["Tanggal"])
    return df

data = load_data()

st.set_page_config(page_title="FinTrack Dashboard", layout="wide")
st.sidebar.title("📊 FinTrack")
st.sidebar.success("Pilih halaman di atas.")

st.title("🏠 Dashboard Keuangan")

if st.button("➕ Catat Transaksi Baru"):
    st.info("Fitur ini akan ditambahkan nanti.")

pemasukan = data[data["Jenis"] == "Pemasukan"]["Jumlah"].sum()
pengeluaran = data[data["Jenis"] == "Pengeluaran"]["Jumlah"].sum()
saldo_bersih = pemasukan - pengeluaran

target_tabungan = 1000000
tabungan_aktual = data[data["Kategori"] == "Tabungan"]["Jumlah"].sum()
progress_tabungan = tabungan_aktual / target_tabungan * 100

total_pendapatan = pemasukan
alokasi_kebutuhan = total_pendapatan * 0.5
alokasi_keinginan = total_pendapatan * 0.3

pengeluaran_kebutuhan = data[data["Kategori"] == "Kebutuhan"]["Jumlah"].sum()
pengeluaran_keinginan = data[data["Kategori"] == "Keinginan"]["Jumlah"].sum()
sisa_anggaran = (alokasi_kebutuhan - pengeluaran_kebutuhan) + (alokasi_keinginan - pengeluaran_keinginan)

col1, col2, col3 = st.columns(3)
col1.metric("💰 Saldo Bersih", f"Rp {saldo_bersih:,.0f}")
col2.metric("📊 Sisa Anggaran 50/30/20", f"Rp {sisa_anggaran:,.0f}")
col3.metric("🎯 Progres Tabungan", f"{progress_tabungan:.1f}%")

data['Bulan'] = data['Tanggal'].dt.to_period('M').astype(str)
trend = data.groupby(['Bulan', 'Jenis'])['Jumlah'].sum().reset_index()
fig = px.line(trend, x='Bulan', y='Jumlah', color='Jenis', title='Tren Keuangan Bulanan')
st.plotly_chart(fig, use_container_width=True)
