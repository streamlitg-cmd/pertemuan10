import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("Pertemuan 10: Interaksi Streamlit dan Yahoo Finance")

kamus_ticker = {
    "GOOGL":'Google',
    'AAPL': 'Apple Inc',
    'SBUX': 'Starbucks',
    'MCD': "McDonanld Corps",
    'META': "Meta Platform Inc",
    'TLK.JK': "Telkom Indonesia",
    'BBNI.JK': 'Bank Negara Indonesia',
    'BMRI.JK': 'Bank Mandiri (Persero) Tbk PT',
    'BBRI.JK': 'Bank Rakyat Indonesia (Persero) Tbk PT',
    'NESN': 'Nestle SA'
}

ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    sorted( kamus_ticker.keys() )
)


st.write(ticker_symbol)

ticker_data = yf.Ticker( ticker_symbol )
pilihan_periode = st.selectbox(
    'Pilih periode',
    ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y',]
)
tgl_mulai = st.date_input(
    'Mulai tanggal',
    value=date.today()
)
tgl_akhir = st.date_input(
    'Sampai tanggal',
    value=date.today()
)
st.write(tgl_mulai)
st.write(tgl_akhir)

df_ticker = ticker_data.history(
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

pilihan_tampil_tabel = st.checkbox('Tampilkan tabel')

if pilihan_tampil_tabel == True:
    st.write("## Lima Data Awal")
    st.write( df_ticker.head() )

st.write(f"## Visualisasi Pergerakan Saham{kamus_ticker[ticker_symbol]}")

pilihan_atribut = st.multiselect(
    'Silakan pilih atribut yang akan ditampilkan:',
    ['Low', 'High', 'Open', 'Close', 'Volime']
)
#st.write(pilihan_atribut)
grafik = px.line(
    df_ticker,
    y=pilihan_atribut,
    title=f"HarGA Saham (kamus_ticker{ticker_symbol})"
)
st.plotly_chart( grafik )
