import streamlit as st
import pandas as pd

csv_path = "journal.csv"

st.header("📈 Trade History")
df_journal = pd.read_csv(csv_path)
st.dataframe(df_journal.sort_values(by="Timestamp", ascending=False), use_container_width=True)