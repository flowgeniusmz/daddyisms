import streamlit as st
import requests

# Single webhook URL
url = "https://discord.com/api/webhooks/1362061287856541897/r7Bma3wlnjwNUKpsb2-zYYXTjGyQlZrGI1Rhqw7SvkNSUubysMmhN8z5jF3mwO-tsGBL"

# User input
content = st.text_input(label="Alert")
decision = st.selectbox("Decision", ["Yes", "No"])

# Submit button
button = st.button(label="Submit")
if button and content.strip():
    full_message = f"{content}\nDecision: {decision}"
    payload = {"content": full_message}
    response = requests.post(url=url, json=payload)
    st.write(f"Sent! Status: {response.status_code}")
