import streamlit as st
import pandas as pd

df = pd.read_csv("sales_data.csv")

st.title("📊 Regional Sales Dashboard")

month = st.selectbox("Select Month", df['Month'].unique())
filtered = df[df['Month'] == month]

st.bar_chart(filtered.groupby("Region")["Revenue ($)"].sum())
