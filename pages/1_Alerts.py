import streamlit as st
import requests

url1 = st.secrets.webhooks.alerts1
url2 = st.secrets.webhooks.alerts2
url3 = st.secrets.webhooks.alerts3

urls = [url1, url2, url3]


content = st.text_input(label="Alert")

button = st.button(label="Submit")
if button:
    payload = {"content": f"@everyone {content}"}
    for url in urls:
        response = requests.post(url=url, json=payload)
        print(response)
