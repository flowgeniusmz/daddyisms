import streamlit as st
import pandas as pd

csv_path = "journal.csv"

df_journal = pd.read_csv(csv_path)

total_trades = len(df_journal)
wins = df_journal[df_journal['Result'] == 'Win']
losses = df_journal[df_journal['Result'] == 'Loss']
total_wins = len(wins)
total_losses = len(losses)
win_percent = (total_wins / total_trades * 100) if total_trades > 0 else 0
loss_percent = (total_losses / total_trades * 100) if total_trades > 0 else 0
avg_win_percent = wins["% Change"].mean() if total_wins > 0 else 0
avg_loss_percent = losses['% Change'].mean() if total_losses > 0 else 0

st.header("📈 Trade History")
st.subheader("Summary Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Wins", f"{total_wins} ({win_percent:.1f}%)")
col2.metric("Total Losses", f"{total_losses} ({loss_percent:.1f}%)")
col3.metric("Avg Win %", f"{avg_win_percent:.2f}%")
col4.metric("Avg Loss %", f"{avg_loss_percent:.2f}%")
st.divider()
st.subheader("Trade Journal")


st.dataframe(df_journal.sort_values(by="Timestamp", ascending=False), use_container_width=True)