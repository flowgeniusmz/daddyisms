import streamlit as st
import requests

# Webhook URL
url = "https://discord.com/api/webhooks/1362061287856541897/r7Bma3wlnjwNUKpsb2-zYYXTjGyQlZrGI1Rhqw7SvkNSUubysMmhN8z5jF3mwO-tsGBL"

# --- Inputs ---
content = st.text_input("Alert")
entry_price = st.number_input("Entry Price", min_value=0.0, format="%.2f")
exit_price = st.number_input("Exit Price", min_value=0.0, format="%.2f")
target_price = st.number_input("Target Price", min_value=0.0, format="%.2f")
trailing_stop_pct = st.number_input("Trailing Stop %", min_value=0.0, max_value=100.0, format="%.2f")

# --- Calculations ---
percent_change = None
result = None
emoji = ""
trailing_stop_price = None
risk_reward_ratio = None

if entry_price > 0:
    # Result & % Change
    percent_change = ((exit_price - entry_price) / entry_price) * 100
    if exit_price > entry_price:
        result = "Win"
        emoji = "🟢"
    elif exit_price < entry_price:
        result = "Loss"
        emoji = "🔴"
    else:
        result = "Break Even"
        emoji = "⚪"

    # Trailing stop price
    trailing_stop_price = entry_price * (1 - trailing_stop_pct / 100)

    # Risk-to-reward ratio
    if target_price > entry_price:
        risk = entry_price - trailing_stop_price
        reward = target_price - entry_price
        if risk > 0:
            risk_reward_ratio = reward / risk

# --- Display Results ---
if result:
    st.markdown(f"**Result:** {emoji} {result}")
    st.markdown(f"**Change:** {percent_change:.2f}%")
    st.markdown(f"**Trailing Stop Price:** ${trailing_stop_price:.2f}")
    if risk_reward_ratio:
        st.markdown(f"**Risk-to-Reward Ratio:** {risk_reward_ratio:.2f}")

# --- Submit ---
if st.button("Submit") and content.strip() and result:
    full_message = (
        f"{content}\n"
        f"Result: {emoji} {result}\n"
        f"Entry Price: ${entry_price:.2f}\n"
        f"Exit Price: ${exit_price:.2f}\n"
        f"Change: {percent_change:.2f}%\n"
        f"Trailing Stop @ {trailing_stop_pct:.2f}%: ${trailing_stop_price:.2f}\n"
    )
    if risk_reward_ratio:
        full_message += f"Risk-to-Reward Ratio: {risk_reward_ratio:.2f}"

    payload = {"content": full_message}
    response = requests.post(url=url, json=payload)
    st.success(f"Sent! Status: {response.status_code}")
