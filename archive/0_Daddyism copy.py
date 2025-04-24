import streamlit as st
import requests
import tempfile

st.set_page_config(layout="wide")

# Discord Webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1360719040682660162/5AdyoOsvOJgwIGAs4JNC_9LFaEFN2-l9Zg8LF8-0IcmFTpi7d7xmaPIBLELjcwuR-QF1"

st.title("📤 Daddyism Discord Uploader")

# Input fields
blurb = st.text_input("💬 Enter your Daddyism blurb:", "Do you even trend, bro?")
uploaded_file = st.file_uploader("📎 Upload your image (PNG only)", type=["png"])

# Submit button
if st.button("🚀 Send to Discord"):
    if not uploaded_file:
        st.error("👊 Upload an image first, Daddy.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        with open(tmp_file_path, "rb") as f:
            files = {
                'payload_json': (None, f'{{"content": "{blurb}"}}'),
                'file1': (uploaded_file.name, f, "image/png")
            }

            response = requests.post(DISCORD_WEBHOOK_URL, files=files)

        if response.status_code == 204 or response.status_code == 200:
            st.success("✅ Daddyism sent to Discord!")
        else:
            st.error(f"❌ Failed to send: {response.status_code}\n{response.text}")
