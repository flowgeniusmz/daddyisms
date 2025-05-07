import streamlit as st
from openai import OpenAI
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime
from prompts import watchlist_prompt, watchlist_prompt2, watchlist_template
from typing import Literal

# 1. SETUP 
#### 1A. General
today = datetime.date.today().strftime("%Y-%m-%d")
tickers = st.secrets.tickers.ticker_list

#### 1B. OpenAI
client = OpenAI(api_key=st.secrets.openai.api_key)
sys_prompt = watchlist_prompt()
sys_prompt2 = watchlist_prompt2()
user_prompt = f"Please provide the watchlist for today ({today})."
input = [{"role": "system", "content": f"{sys_prompt2}"}, {"role": "user", "content": f"{user_prompt}"}]
web_tool = {"type": "web_search_preview","user_location": {"type": "approximate","country": "US"},"search_context_size": "high"}
tools = [web_tool]
#tool_choice = {"type": "web_search_preview"}
tool_choice = "required"
model = "gpt-4.1"
temperature = .1
max_output_tokens = 16000

#### 1C. Discord Webhook
url = st.secrets.discord.watchlist_url
logo_path = "logo.png"
title = f"Watchlist - {today}"
color = "03b2f8"
webhook = DiscordWebhook(url=url)

# 2. FUNCTIONS
#### 2A. Get Watchlist from OpenAI
def get_watchlist():
    response = client.responses.create(
        model=model,
        input=input,
        tools=tools,
        tool_choice=tool_choice,
        temperature=temperature,
        max_output_tokens=max_output_tokens
    )
    response_output = response.output_text
    return response_output

#### 2B. Set and send Discord Embed
def set_send_embed(description: str, type: Literal["ai", "human"]):
    if type == "ai":
        author = "Daddy Trades AI"
    else:
        author = "Daddy's Watchlist"

    embed = DiscordEmbed(title=title, description=description, color=color)
    embed.set_author(name=author)#, url="author url", icon_url="author icon url")
    # embed.set_image(url="your image url")
    # embed.set_thumbnail(url="your thumbnail url")
    # embed.set_footer(text="Embed Footer Text", icon_url="URL of icon")
    # embed.set_timestamp()
    # embed.add_embed_field(name="Field 1", value="Lorem ipsum")
    # embed.add_embed_field(name="Field 2", value="dolor sit")
    webhook.add_embed(embed=embed)
    response = webhook.execute()
    print(response)
    return response.status_code in [200, 204]

# DISPLAY
# 3. STREAMLIT APP UI
st.title("📈 Daily Options Watchlist Generator")
st.markdown("Generate and review today's top 5 tickers for day trading options, then send it to Discord.")

# Session state for generated response
if "watchlist" not in st.session_state:
    st.session_state.watchlist = ""

# Button to generate
if st.button("🧠 Generate Watchlist with OpenAI"):
    with st.spinner("Calling OpenAI and performing web search..."):
        try:
            result = get_watchlist()
            st.session_state.watchlist = result
            st.success("Watchlist generated!")
        except Exception as e:
            st.error(f"Error: {e}")

# Display generated output
if st.session_state.watchlist:
    st.subheader("📝 Watchlist Preview")
    st.markdown(st.session_state.watchlist)
    #st.text_area("OpenAI Response", st.session_state.watchlist, height=400)

    # Approval and send
    if st.button("✅ Approve and Send to Discord"):
        with st.spinner("Sending to Discord..."):
            try:
                success = set_send_embed(description=f"{st.session_state.watchlist}", type="ai")
                if success:
                    st.success("📤 Successfully posted to Discord!")
                else:
                    st.error("❌ Failed to send to Discord.")
            except Exception as e:
                st.error(f"Error: {e}")
    
    # Additional section: Manual Watchlist Submission
    st.subheader("✍️ Manually Write and Send Watchlist")
    manual_watchlist = st.text_area("Enter your custom watchlist message for Discord", value=watchlist_template(), height=300)

    if st.button("📨 Send Manual Watchlist to Discord"):
        if manual_watchlist.strip() == "":
            st.warning("Please enter a message before sending.")
        else:
            with st.spinner("Sending manual watchlist to Discord..."):
                try:
                    success = set_send_embed(manual_watchlist, type="human")
                    if success:
                        st.success("📤 Manual watchlist sent to Discord!")
                    else:
                        st.error("❌ Failed to send manual watchlist.")
                except Exception as e:
                    st.error(f"Error: {e}")



