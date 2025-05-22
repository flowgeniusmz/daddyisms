import streamlit as st
import prompts as p
from openai import OpenAI
import base64
import tempfile
import requests
from pydantic import BaseModel

# OpenAI Client Setup
client = OpenAI(api_key=st.secrets.openai.api_key)
model_image = "gpt-image-1"
model_chat = "gpt-4.1"
daddyism_prompt = p.daddyism_prompt()

url1 = st.secrets.webhooks.daddyisms
url2 = st.secrets.webhooks.daddyisms2

urls = [url1, url2]

# Pydantic Model
class Daddyism(BaseModel):
    title: str
    category: str
    daddyism: str
    memedescription: str
    topcaption: str
    bottomcaption: str

# Image Generator
def generate_image(prompt: str):
    result = client.images.generate(
        model=model_image,
        prompt=prompt
    )
    result_base64 = result.data[0].b64_json
    return base64.b64decode(result_base64)


def post_to_discord(image_bytes: bytes, message: str, filename: str = "daddyism.png") -> bool:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        tmp_file.write(image_bytes)
        tmp_file_path = tmp_file.name

    success = True
    with open(tmp_file_path, "rb") as f:
        files = {
            'payload_json': (None, f'{{"content": "{message}"}}'),
            'file1': (filename, f, "image/png")
        }
        for url in urls:
            response = requests.post(url=url, files=files)
            if response.status_code not in [200, 204]:
                success = False  # Mark as failed if any request fails

    return success

# # Meme Poster
# def post_to_discord(image_bytes: bytes, message: str, filename: str = "daddyism.png") -> bool:
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
#         tmp_file.write(image_bytes)
#         tmp_file_path = tmp_file.name

#     with open(tmp_file_path, "rb") as f:
#         files = {
#             'payload_json': (None, f'{{"content": "{message}"}}'),
#             'file1': (filename, f, "image/png")
#         }
#         for url in urls:
#             response = requests.post(url=url, files=files)

#             return response.status_code in [200, 204]

# Daddyism Generator
def generate_daddyism():
    messages = [
        {"role": "system", "content": daddyism_prompt},
        {"role": "user", "content": "Create a daddyism"}
    ]
    response = client.responses.parse(
        input=messages,
        model=model_chat,
        text_format=Daddyism
    )
    return response.output_parsed

# UI
st.title("Daddyism Meme Generator")
st.divider()

# Generate button
if st.button("Generate Daddyism"):
    with st.spinner("Summoning Daddy Trades..."):
        generated = generate_daddyism()
        st.session_state.generated = generated

# Form to display and edit
if "generated" in st.session_state:
    d = st.session_state.generated

    st.subheader("📋 Review & Edit")

    title_text = st.text_input("Title", value=d.title)
    category_text = st.text_input("Category", value=d.category)
    daddyism_text = st.text_input("Daddyism", value=d.daddyism)
    meme_description_text = st.text_input("Meme Description", value=d.memedescription)
    top_caption_text = st.text_input("Top Caption", value=d.topcaption)
    bottom_caption_text = st.text_input("Bottom Caption", value=d.bottomcaption)

    # Meme generation
    if st.button("Generate Meme Image"):
        prompt_image = p.daddyism_meme_prompt(
            title=title_text,
            category=category_text,
            daddyism=daddyism_text,
            meme_description=meme_description_text,
            top_caption=top_caption_text,
            bottom_caption=bottom_caption_text
        )

        with st.spinner("Rendering Meme..."):
            image_bytes = generate_image(prompt_image)

        with st.spinner("Sending to Discord..."):
            success = post_to_discord(image_bytes, message=daddyism_text)

        if success:
            st.success("✅ Meme sent to Discord!")
            st.image(image_bytes, caption=title_text)
            st.download_button(
                label="Download Meme as PNG",
                data=image_bytes,
                file_name=f"{title_text.replace(' ', '_').lower()}.png",
                mime="image/png"
            )
        else:
            st.error("❌ Failed to send meme to Discord.")

