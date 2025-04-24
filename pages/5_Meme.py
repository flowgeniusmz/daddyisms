import streamlit as st
import prompts as p
from openai import OpenAI
import base64

client = OpenAI(api_key=st.secrets.openai.api_key)
model_image = "gpt-image-1"
model_chat = "gpt-4.1"
# prompt_system = p.daddyism_prompt()
# prompt_meme = p.daddyism_meme_prompt()
title = "Theta Trashfire"
category = "Options"
daddyism = "Holding zero-day calls like theyre a retirement plan? Thats not conviction - its financial arson."
meme_description = "Daddy Trades, wide-eyed and sweating, clutches a flaming options contract while sitting on a ticking time bomb labeled “0DTE.” The background is a dumpster fire with stock tickers flying out of it."
top_caption = "HOLDING 0DTE CALLS WITH NO EXIT PLAN"
bottom_caption = "CONGRATS, YOU BOUGHT TIME DECAY AND HOPIUM."

prompt = p.daddyism_meme_prompt(title=title, category=category, daddyism=daddyism, meme_description=meme_description, top_caption=top_caption, bottom_caption=bottom_caption)

def generate_image(prompt: str):
    result = client.images.generate(
        model=model_image,
        prompt=prompt
    )
    result_base64 = result.data[0].b64_json
    result_bytes = base64.b64decode(result_base64)
    return result_bytes

st.title("Daddyism Meme Generator")
st.divider()
btn_generate = st.button("Generate Image")
if btn_generate:
    meme_bytes = generate_image(prompt=prompt)
    st.image(meme_bytes)




