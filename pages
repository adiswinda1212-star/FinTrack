import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Anggaran (50/30/20)")

df = pd.read_csv("data/transactions.csv")

kategori_summary = df[df["Jenis"] == "Pengeluaran"].groupby("Kategori")["Jumlah"].sum().reset_index()
fig = px.pie(kategori_summary, names='Kategori', values='Jumlah', title='Distribusi Pengeluaran', hole=0.4)
st.plotly_chart(fig)

st.subheader("📄 Riwayat Transaksi")
st.dataframe(df)
