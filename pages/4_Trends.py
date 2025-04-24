import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Load data
csv_path = "journal.csv"
df_journal = pd.read_csv(csv_path)

# Convert Timestamp to datetime
df_journal['Timestamp'] = pd.to_datetime(df_journal['Timestamp'])

# Calculate week numbers and years
df_journal['Year'] = df_journal['Timestamp'].dt.isocalendar().year
df_journal['Week'] = df_journal['Timestamp'].dt.isocalendar().week

# Get current date and week
current_date = datetime.now()
current_year = current_date.isocalendar().year
current_week = current_date.isocalendar().week
previous_week = current_week - 1 if current_week > 1 else 52
previous_year = current_year if current_week > 1 else current_year - 1

# Filter data for current and previous week
current_week_data = df_journal[(df_journal['Year'] == current_year) & (df_journal['Week'] == current_week)]
previous_week_data = df_journal[(df_journal['Year'] == previous_year) & (df_journal['Week'] == previous_week)]

# Function to calculate weekly stats
def calculate_weekly_stats(df):
    total_trades = len(df)
    wins = df[df['Result'] == 'Win']
    losses = df[df['Result'] == 'Loss']
    total_wins = len(wins)
    total_losses = len(losses)
    win_percent = (total_wins / total_trades * 100) if total_trades > 0 else 0
    net_trades = total_wins - total_losses
    cumulative_profit = (df['Exit Price'].sum() - df['Entry Price'].sum()) if total_trades > 0 else 0
    return {
        'total_trades': total_trades,
        'wins': total_wins,
        'losses': total_losses,
        'win_percent': win_percent,
        'net_trades': net_trades,
        'cumulative_profit': cumulative_profit
    }

# Calculate stats
current_stats = calculate_weekly_stats(current_week_data)
previous_stats = calculate_weekly_stats(previous_week_data)

# Display
st.header("📅 Weekly Trade Analysis")

# Current Week Stats
st.subheader(f"Current Week (Week {current_week}, {current_year})")
col1, col2, col3 = st.columns(3)
col1.metric("Total Trades", current_stats['total_trades'])
col2.metric("Wins", f"{current_stats['wins']} ({current_stats['win_percent']:.1f}%)")
col3.metric("Net Trades (W-L)", current_stats['net_trades'])
col1.metric("Losses", current_stats['losses'])
col2.metric("Cumulative Profit", f"${current_stats['cumulative_profit']:.2f}")
st.divider()

# Previous Week Stats
st.subheader(f"Previous Week (Week {previous_week}, {previous_year})")
col1, col2, col3 = st.columns(3)
col1.metric("Total Trades", previous_stats['total_trades'])
col2.metric("Wins", f"{previous_stats['wins']} ({previous_stats['win_percent']:.1f}%)")
col3.metric("Net Trades (W-L)", previous_stats['net_trades'])
col1.metric("Losses", previous_stats['losses'])
col2.metric("Cumulative Profit", f"${previous_stats['cumulative_profit']:.2f}")
st.divider()

# Week-over-Week Trends
st.subheader("Week-over-Week Trends")
weekly_stats = df_journal.groupby(['Year', 'Week']).apply(
    lambda x: pd.Series({
        'Total Trades': len(x),
        'Wins': len(x[x['Result'] == 'Win']),
        'Losses': len(x[x['Result'] == 'Loss']),
        'Win Percent': (len(x[x['Result'] == 'Win']) / len(x) * 100) if len(x) > 0 else 0,
        'Net Trades': len(x[x['Result'] == 'Win']) - len(x[x['Result'] == 'Loss']),
        'Cumulative Profit': (x['Exit Price'].sum() - x['Entry Price'].sum())
    })
).reset_index()

# Create plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
weekly_stats['Week_Label'] = weekly_stats.apply(lambda x: f"{int(x['Year'])}-W{int(x['Week']):02d}", axis=1)

# Plot Net Trades
ax1.plot(weekly_stats['Week_Label'], weekly_stats['Net Trades'], marker='o', color='blue')
ax1.set_title('Net Trades (Wins - Losses) by Week')
ax1.set_xlabel('Week')
ax1.set_ylabel('Net Trades')
ax1.grid(True)
ax1.tick_params(axis='x', rotation=45)

# Plot Cumulative Profit
ax2.plot(weekly_stats['Week_Label'], weekly_stats['Cumulative Profit'], marker='o', color='green')
ax2.set_title('Cumulative Profit by Week')
ax2.set_xlabel('Week')
ax2.set_ylabel('Profit ($)')
ax2.grid(True)
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
st.pyplot(fig)

# Display weekly stats table
st.subheader("All Weeks Summary")
st.dataframe(
    weekly_stats[['Year', 'Week', 'Total Trades', 'Wins', 'Losses', 'Win Percent', 'Net Trades', 'Cumulative Profit']]
    .sort_values(['Year', 'Week'], ascending=False),
    use_container_width=True
)