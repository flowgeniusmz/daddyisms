import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)
model = "dall-e-3"
size = "1024x1024"
quality="standard"

prompt_instructions = "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:"
prompt_persona = "Persona: Daddy Trades is alight-skinned cartoon character with black hair, mustache, sunglasses, teal shirt, and gold crown—include (think Randy Marsh). Daddy Trades is a trading-savvy, irreverent, no-nonsense father figure (inspired by Randy Marsh with shades and a crown). Daddyisms reflect his confident, sarcastic, sometimes savage commentary on the market and trader behavior."

def generate_meme(prompt: str):
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        n=1,
        quality=quality
    )
    url = response.data[0].url
    return url

