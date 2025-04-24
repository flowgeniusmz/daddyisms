import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime

# --- Configuration ---

# Alert webhooks
discord_url_1 = "https://discord.com/api/webhooks/1362095902571106565/heUGL91PIzpa1Ah1KMY1KaBpW9vGSGwhRqDZULnTQYuErNEsK09p1c1bx_-Baou_RgYp"
discord_url_2 = "https://discord.com/api/webhooks/1360719025696669756/kj7Ud2DolXNDdyZPcoUIzZoMFPP_mhNmRNT2fkvaS-XCEykgcwhPVEvLnzbSIPLpqQkg"
discord_url_3 = "https://discord.com/api/webhooks/1362055824310276356/4fMbGvXG9uS-C4tF-sg4obfO-FrVhFbog0d7s6y3Dqp_yPhF8B1C8bnmA_O_EPgO372f"
discord_url_4 = "https://discord.com/api/webhooks/1362104938582245386/5vzPMLTUMG8Q5X2vW6q-9X7-9ZrSNzM01Hx796ORbD4_Y4tl3NZtkI_G0jhvS9vLExhE"
alert_urls = [discord_url_1, discord_url_2, discord_url_3, discord_url_4]

# Journal webhooks
url1 = "https://discord.com/api/webhooks/1362061287856541897/r7Bma3wlnjwNUKpsb2-zYYXTjGyQlZrGI1Rhqw7SvkNSUubysMmhN8z5jF3mwO-tsGBL"
url2 = "https://discord.com/api/webhooks/1362144062244651161/-gIpndW2OncFgB4PaEsStrDypBBO6VZZXpCtU3BU6rpj6vUOg87BOy2NFKdDeXBcxi1e"
journal_urls = [url1, url2]

# CSV path (will be created if missing)
csv_path = "journal.csv"


# --- Session State Setup ---
if "alert_sent" not in st.session_state:
    st.session_state.alert_sent = False
    st.session_state.content = ""
    st.session_state.entry_price = 0.0

st.title("📊 Trading Journal & Alerts")

# --- Stage 1: Send Alert ---
if not st.session_state.alert_sent:
    st.subheader("1. Send Trade Alert")
    content = st.text_input("Alert")
    entry_price = st.number_input("Entry Price", min_value=0.0, format="%.2f")
    if st.button("Send Alert") and content.strip() and entry_price > 0:
        payload = {"content": f"@everyone {content} | Entry Price: ${entry_price:.2f}"}
        for url in alert_urls:
            requests.post(url=url, json=payload)
        st.success("✅ Alert sent!")
        st.session_state.alert_sent = True
        st.session_state.content = content
        st.session_state.entry_price = entry_price
        #st.experimental_rerun()

# --- Stage 2: Complete Journal Entry ---
if st.session_state.alert_sent:
    st.subheader("2. Complete Journal Entry")
    content = st.session_state.content
    entry_price = st.session_state.entry_price
    exit_price = st.number_input("Exit Price", min_value=0.0, format="%.2f")
    percent_change = None
    result = None
    emoji = ""
    color = 0

    if exit_price > 0:
        percent_change = ((exit_price - entry_price) / entry_price) * 100
        if exit_price > entry_price:
            result, emoji, color = "Win", "🟢", 0x00ff00
        elif exit_price < entry_price:
            result, emoji, color = "Loss", "🔴", 0xff0000
        else:
            result, emoji, color = "Break Even", "⚪", 0xcccccc

    if result:
        st.markdown(f"**Result:** {emoji} {result}")
        st.markdown(f"**Change:** {percent_change:.2f}%")

    if st.button("Submit Journal") and result:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        journal_entry = {
            "Timestamp": timestamp,
            "Alert": content,
            "Result": result,
            "Emoji": emoji,
            "Entry Price": round(entry_price, 2),
            "Exit Price": round(exit_price, 2),
            "% Change": round(percent_change, 2),
        }
        # Append to CSV
        with open(csv_path, mode="a", newline='', encoding='utf-8') as f:
            pd.DataFrame([journal_entry]).to_csv(f, header=False, index=False)
        # Send embed to Discord
        embed_payload = {
            "embeds": [
                {
                    "title": f"{emoji} Trade Alert",
                    "description": f"**{content}**",
                    "color": color,
                    "fields": [
                        {"name": "Result", "value": result, "inline": True},
                        {"name": "Entry Price", "value": f"${entry_price:.2f}", "inline": True},
                        {"name": "Exit Price", "value": f"${exit_price:.2f}", "inline": True},
                        {"name": "Change", "value": f"{percent_change:.2f}%", "inline": True},
                    ],
                    "timestamp": datetime.utcnow().isoformat(),
                }
            ]
        }
        for url in journal_urls:
            requests.post(url=url, json=embed_payload)
        st.success("✅ Journal entry submitted!")
        # Reset for next trade
        st.session_state.alert_sent = False
        #st.experimental_rerun()

# --- Display Journal History ---
st.markdown("---")
st.header("📈 Trade History")
df_journal = pd.read_csv(csv_path)
st.dataframe(df_journal.sort_values(by="Timestamp", ascending=False), use_container_width=True)
