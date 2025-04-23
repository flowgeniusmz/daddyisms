import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime

# # Ensure persistent directory exists
# os.makedirs("data", exist_ok=True)
# csv_path = os.path.join("data", "journal.csv")

# # Create file if it doesn't exist
# if not os.path.exists(csv_path):
#     pd.DataFrame(columns=["Timestamp", "Alert", "Result", "Emoji", "Entry Price", "Exit Price", "% Change"]).to_csv(csv_path, index=False)

path = "journal.csv"


# Webhook URLs
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
emoji = ""

if entry_price > 0:
    percent_change = ((exit_price - entry_price) / entry_price) * 100
    if exit_price > entry_price:
        result = "Win"
        emoji = "🟢"
        color = 0x00ff00
    elif exit_price < entry_price:
        result = "Loss"
        emoji = "🔴"
        color = 0xff0000
    else:
        result = "Break Even"
        emoji = "⚪"
        color = 0xcccccc

if result:
    st.markdown(f"**Result:** {emoji} {result}")
    st.markdown(f"**Change:** {percent_change:.2f}%")

if st.button("Submit") and content.strip() and result:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    journal_entry = {
        "Timestamp": timestamp,
        "Alert": content,
        "Result": result,
        "Emoji": emoji,
        "Entry Price": round(entry_price, 2),
        "Exit Price": round(exit_price, 2),
        "% Change": round(percent_change, 2)
    }

    # Append new entry directly to file
    with open(path, mode="a", newline='', encoding='utf-8') as f:
        pd.DataFrame([journal_entry]).to_csv(f, header=False, index=False)

    # Discord Embed Payload
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
                "timestamp": datetime.utcnow().isoformat()
            }
        ]
    }

    for url in urls:
        response = requests.post(url, json=embed_payload)
        st.success(f"Sent! Status: {response.status_code}")

# --- Display Journal ---
st.divider()
st.header("📈 Trade History")
df_journal = pd.read_csv(path)
st.dataframe(df_journal.sort_values(by="Timestamp", ascending=False), use_container_width=True)



# import streamlit as st
# import requests
# import pandas as pd
# import os
# from datetime import datetime

# csv_path = "journal.csv"

# # Webhook URLs
# url1 = "https://discord.com/api/webhooks/1362061287856541897/r7Bma3wlnjwNUKpsb2-zYYXTjGyQlZrGI1Rhqw7SvkNSUubysMmhN8z5jF3mwO-tsGBL"
# url2 = "https://discord.com/api/webhooks/1362144062244651161/-gIpndW2OncFgB4PaEsStrDypBBO6VZZXpCtU3BU6rpj6vUOg87BOy2NFKdDeXBcxi1e"
# urls = [url1, url2]

# # Inputs
# content = st.text_input("Alert")
# entry_price = st.number_input("Entry Price", min_value=0.0, format="%.2f")
# exit_price = st.number_input("Exit Price", min_value=0.0, format="%.2f")

# # Calculation logic
# percent_change = None
# result = None
# emoji = ""

# if entry_price > 0:
#     percent_change = ((exit_price - entry_price) / entry_price) * 100
#     if exit_price > entry_price:
#         result = "Win"
#         emoji = "🟢"
#         color = 0x00ff00  # Green
#     elif exit_price < entry_price:
#         result = "Loss"
#         emoji = "🔴"
#         color = 0xff0000  # Red
#     else:
#         result = "Break Even"
#         emoji = "⚪"
#         color = 0xcccccc  # Grey

# # Display calculated result
# if result:
#     st.markdown(f"**Result:** {emoji} {result}")
#     st.markdown(f"**Change:** {percent_change:.2f}%")

# # Submit button
# if st.button("Submit") and content.strip() and result:
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     journal_entry = {
#         "Timestamp": timestamp,
#         "Alert": content,
#         "Result": result,
#         "Emoji": emoji,
#         "Entry Price": round(entry_price, 2),
#         "Exit Price": round(exit_price, 2),
#         "% Change": round(percent_change, 2)
#     }

#     # Update CSV
#     df_existing = pd.read_csv(csv_path)
#     df_new = pd.concat([df_existing, pd.DataFrame([journal_entry])], ignore_index=True)
#     df_new.to_csv(csv_path, index=False)

#     # Prepare Discord embed payload
#     embed_payload = {
#         "embeds": [
#             {
#                 "title": f"{emoji} Trade Alert",
#                 "description": f"**{content}**",
#                 "color": color,
#                 "fields": [
#                     {"name": "Result", "value": result, "inline": True},
#                     {"name": "Entry Price", "value": f"${entry_price:.2f}", "inline": True},
#                     {"name": "Exit Price", "value": f"${exit_price:.2f}", "inline": True},
#                     {"name": "Change", "value": f"{percent_change:.2f}%", "inline": True},
#                 ],
#                 "timestamp": datetime.utcnow().isoformat()
#             }
#         ]
#     }

#     # Send to each webhook
#     for url in urls:
#         response = requests.post(url, json=embed_payload)
#         st.success(f"Sent! Status: {response.status_code}")

# # --- Display Journal ---
# st.divider()
# st.header("📈 Trade History")
# df_journal = pd.read_csv(csv_path)
# st.dataframe(df_journal.sort_values(by="Timestamp", ascending=False), use_container_width=True)



# import streamlit as st
# import requests
# import pandas as pd
# import os
# from datetime import datetime

# csv_path = "journal.csv"


# # Webhook URL
# url1 = "https://discord.com/api/webhooks/1362061287856541897/r7Bma3wlnjwNUKpsb2-zYYXTjGyQlZrGI1Rhqw7SvkNSUubysMmhN8z5jF3mwO-tsGBL"
# url2 = "https://discord.com/api/webhooks/1362144062244651161/-gIpndW2OncFgB4PaEsStrDypBBO6VZZXpCtU3BU6rpj6vUOg87BOy2NFKdDeXBcxi1e"
# urls = [url1, url2]

# # Inputs
# content = st.text_input("Alert")
# entry_price = st.number_input("Entry Price", min_value=0.0, format="%.2f")
# exit_price = st.number_input("Exit Price", min_value=0.0, format="%.2f")

# # Calculation logic
# percent_change = None
# result = None

# if entry_price > 0:
#     # Result & % Change
#     percent_change = ((exit_price - entry_price) / entry_price) * 100
#     if exit_price > entry_price:
#         result = "Win"
#         emoji = "🟢"
#     elif exit_price < entry_price:
#         result = "Loss"
#         emoji = "🔴"
#     else:
#         result = "Break Even"
#         emoji = "⚪"

# # Display calculated result
# if result:
#     st.markdown(f"**Result:** {emoji} {result}")
#     st.markdown(f"**Change:** {percent_change:.2f}%")

# # Submit button
# if st.button("Submit") and content.strip() and result:
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     journal_entry = {
#         "Timestamp": timestamp,
#         "Alert": content,
#         "Result": result,
#         "Emoji": emoji,
#         "Entry Price": round(entry_price, 2),
#         "Exit Price": round(exit_price, 2),
#         "% Change": round(percent_change, 2)
#     }
#     df_existing = pd.read_csv(csv_path)
#     df_new = pd.concat([df_existing, pd.DataFrame([journal_entry])], ignore_index=True)
#     df_new.to_csv(csv_path, index=False)

#     full_message = (
#         f"{content}\n"
#         f"Result: {result}\n"
#         f"Entry Price: ${entry_price:.2f}\n"
#         f"Exit Price: ${exit_price:.2f}\n"
#         f"Change: {percent_change:.2f}%"
#     )
#     payload = {"content": full_message}
#     for url in urls:
#         response = requests.post(url=url, json=payload)
#         st.success(f"Sent! Status: {response.status_code}")

# # --- Display Journal ---
# st.divider()
# st.header("📈 Trade History")
# df_journal = pd.read_csv(csv_path)
# st.dataframe(df_journal.sort_values(by="Timestamp", ascending=False), use_container_width=True)
