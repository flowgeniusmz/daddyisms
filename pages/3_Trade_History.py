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
biggest_win = wins["% Change"].max() if total_wins > 0 else 0
biggest_loss = losses["% Change"].min() if total_losses > 0 else 0
cumulative_exit = (df_journal['Exit Price'].sum()) if total_trades > 0 else 0
cumulative_entry = (df_journal['Entry Price'].sum()) if total_trades > 0 else 0
cumulative_profit = (df_journal['Exit Price'].sum() - df_journal['Entry Price'].sum()) if total_trades > 0 else 0

st.header("📈 Trade History")
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Wins", f"{total_wins} ({win_percent:.1f}%)")
col2.metric("Total Losses", f"{total_losses} ({loss_percent:.1f}%)")
col3.metric("Avg Win %", f"{avg_win_percent:.2f}%")
col1.metric("Avg Loss %", f"{avg_loss_percent:.2f}%")
col2.metric("Biggest Win", f"{biggest_win:.2f}%")
col3.metric("Biggest Loss", f"{biggest_loss:.2f}%")

st.divider()
st.subheader("Cumulative Statistics")
st.caption("Assumes a quantity of 1 option per trade. Cumulative Profit = Cumulative Exit - Cumulative Entry.")
col1, col2, col3 = st.columns(3)
col1.metric("Cumulative Exit", f"${cumulative_exit:.2f}")
col2.metric("Cumulative Entry", f"${cumulative_entry:.2f}")
col3.metric("Cumulative Profit", f"${cumulative_profit:.2f}")

st.divider()
st.subheader("Scenario Statistics")
st.caption("Set position size per trade. Profit per trade = Position Size * (% Change / 100).")
position_size = st.number_input("Position Size ($)", min_value=0.0, value=100.0, step=10.0)
scenario_entry = position_size * total_trades if total_trades > 0 else 0
scenario_exit = (position_size * (1 + df_journal['% Change'] / 100)).sum() if total_trades > 0 else 0
scenario_profit = (df_journal['% Change'] / 100 * position_size).sum() if total_trades > 0 else 0
col1, col2, col3 = st.columns(3)
col1.metric(f"Cumulative Exit (${position_size}/trade)", f"${scenario_exit:.2f}")
col2.metric(f"Cumulative Entry (${position_size}/trade)", f"${scenario_entry:.2f}")
col3.metric(f"Cumulative Profit (${position_size}/trade)", f"${scenario_profit:.2f}")

st.divider()
st.subheader("Trade Journal")

st.dataframe(df_journal.sort_values(by="Timestamp", ascending=False), use_container_width=True)