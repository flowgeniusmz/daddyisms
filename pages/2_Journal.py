import streamlit as st
import requests

# Webhook URL
url1 = "https://discord.com/api/webhooks/1362061287856541897/r7Bma3wlnjwNUKpsb2-zYYXTjGyQlZrGI1Rhqw7SvkNSUubysMmhN8z5jF3mwO-tsGBL"
url2 = "https://discord.com/api/webhooks/1362144062244651161/-gIpndW2OncFgB4PaEsStrDypBBO6VZZXpCtU3BU6rpj6vUOg87BOy2NFKdDeXBcxi1e"
urls = [url1, url2]

# Inputs
content = st.text_input("Alert")
entry_price = st.number_input("Entry Price", min_value=0.0, format="%.2f")
exit_price = st.number_input("Exit Price", min_value=0.0, format="%.2f")

# Calculation logic
percent_change = None
result = None

if entry_price > 0 and exit_price >= 0:
    percent_change = ((exit_price - entry_price) / entry_price) * 100
    if exit_price > entry_price:
        result = "Win"
    elif exit_price < entry_price:
        result = "Loss"
    else:
        result = "Break Even"

# Display calculated result
if result:
    st.markdown(f"**Result:** {result}")
    st.markdown(f"**Change:** {percent_change:.2f}%")

# Submit button
if st.button("Submit") and content.strip() and result:
    full_message = (
        f"{content}\n"
        f"Result: {result}\n"
        f"Entry Price: ${entry_price:.2f}\n"
        f"Exit Price: ${exit_price:.2f}\n"
        f"Change: {percent_change:.2f}%"
    )
    payload = {"content": full_message}
    for url in urls:
        response = requests.post(url=url, json=payload)
        st.success(f"Sent! Status: {response.status_code}")




# import streamlit as st
# import requests

# # Webhook URL
# url = "https://discord.com/api/webhooks/1362061287856541897/r7Bma3wlnjwNUKpsb2-zYYXTjGyQlZrGI1Rhqw7SvkNSUubysMmhN8z5jF3mwO-tsGBL"

# # User inputs
# content = st.text_input(label="Alert")
# result = st.selectbox("Result", ["Win", "Loss"])
# entry_price = st.number_input("Entry Price", min_value=0.0, format="%.2f")
# exit_price = st.number_input("Exit Price", min_value=0.0, format="%.2f")

# # Calculate % gain/loss
# percent_change = None
# if entry_price > 0:
#     percent_change = ((exit_price - entry_price) / entry_price) * 100

# # Submit button
# button = st.button(label="Submit")
# if button and content.strip() and entry_price > 0:
#     full_message = (
#         f"{content}\n"
#         f"Result: {result}\n"
#         f"Entry Price: ${entry_price:.2f}\n"
#         f"Exit Price: ${exit_price:.2f}\n"
#         f"Change: {percent_change:.2f}%"
#     )
#     payload = {"content": full_message}
#     response = requests.post(url=url, json=payload)
#     st.write(f"Sent! Status: {response.status_code}")




# import streamlit as st
# import requests

# # Single webhook URL
# url = "https://discord.com/api/webhooks/1362061287856541897/r7Bma3wlnjwNUKpsb2-zYYXTjGyQlZrGI1Rhqw7SvkNSUubysMmhN8z5jF3mwO-tsGBL"

# # User input
# content = st.text_input(label="Alert")
# result = st.selectbox("Result", ["Win", "Loss"])

# # Submit button
# button = st.button(label="Submit")
# if button and content.strip():
#     full_message = f"{content}\nResult: {result}"
#     payload = {"content": full_message}
#     response = requests.post(url=url, json=payload)
#     st.write(f"Sent! Status: {response.status_code}")
