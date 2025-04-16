import streamlit as st
import requests

#fattybags club
#discord_url_1 = "https://discord.com/api/webhooks/1362055010292203661/EnUAjQWtzCxd8fSHANdg6CMiU-qp_RIwC2za6qazDQ6rK5c4lPi-e9Qod_Cx8SqAwb8Q"
discord_url_1 = "https://discord.com/api/webhooks/1362095902571106565/heUGL91PIzpa1Ah1KMY1KaBpW9vGSGwhRqDZULnTQYuErNEsK09p1c1bx_-Baou_RgYp"

#daddy trades
discord_url_2 = "https://discord.com/api/webhooks/1360719025696669756/kj7Ud2DolXNDdyZPcoUIzZoMFPP_mhNmRNT2fkvaS-XCEykgcwhPVEvLnzbSIPLpqQkg"
discord_url_3 = "https://discord.com/api/webhooks/1362055824310276356/4fMbGvXG9uS-C4tF-sg4obfO-FrVhFbog0d7s6y3Dqp_yPhF8B1C8bnmA_O_EPgO372f"

#rsi rascals
#discord_url_4 = "https://discord.com/api/webhooks/1362055962269323284/A1vYX-rZC2dtO2HkTM9XvlR9cc1arKYrBF7yU2mFfyYsd2U2--rIHn-KTE-A3-yPlupA"
discord_url_4 = "https://discord.com/api/webhooks/1362104938582245386/5vzPMLTUMG8Q5X2vW6q-9X7-9ZrSNzM01Hx796ORbD4_Y4tl3NZtkI_G0jhvS9vLExhE"

urls = [discord_url_1, discord_url_2, discord_url_3, discord_url_4]

content = st.text_input(label="Alert")

button = st.button(label="Submit")
if button:
    payload = {"content": f"@everyone {content}"}
    for url in urls:
        response = requests.post(url=url, json=payload)
        print(response)
