import streamlit as st
import uuid
import pandas as pd

def initialize_session_state():
    if "initialized" not in st.session_state:
        st.session_state.journal_path = st.secrets.paths.journal
        st.session_state.alert_sent = False
        st.session_state.alert_content = ""
        st.session_state.entry_price = 0.0
        st.session_state.exit_price = 0.0
        st.session_state.percent_change = 0.0
        st.session_state.result = ""
        st.session_state.emoji = ""
        st.session_state.color_loss = "0xff0000"
        st.session_state.color_win = "0x00ff00"
        st.session_state.color_be = "0xcccccc"
        st.session_state.emoji_win = "🟢"
        st.session_state.emoji_loss = "🔴"
        st.session_state.emoji_be = "⚪"
        st.session_state.result_win = "Win"
        st.session_state.result_loss = "Loss"
        st.session_state.result_be = "Break Even"
        st.session_state.price_format = "%.2f"
        st.session_state.alert_id = str(uuid.uuid4())
        st.session_state.alert_urls = st.secrets.discord.alert_urls
        st.session_state.journal_urls = st.secrets.discord.journal_urls
        st.session_state.journal_df = pd.read_csv(st.session_state.journal_path)