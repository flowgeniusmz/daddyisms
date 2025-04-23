import streamlit as st
from openai import OpenAI
import base64
from messages import initialmessages
import requests

# Variables
client = OpenAI(api_key=st.secrets.openai.api_key)
text_model = "gpt-4o"
text_tools = [{"type": "web_search_preview"}]
text_input = initialmessages
image_model = "dall-e-3"
image_size = "1024x1024"
image_quality="standard"
image_prompt_instructions = "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:"
image_prompt_persona = "Persona: Daddy Trades is alight-skinned cartoon character with black hair, mustache, sunglasses, teal shirt, and gold crown—include (think Randy Marsh). Daddy Trades is a trading-savvy, irreverent, no-nonsense father figure (inspired by Randy Marsh with shades and a crown). Daddyisms reflect his confident, sarcastic, sometimes savage commentary on the market and trader behavior."

# Functions
def generate_text():
    response = client.responses.create(model=text_model,input=text_input,tools=text_tools,temperature=1,max_output_tokens=2048,top_p=1,store=True)
    output = response.output_text
    return output

def generate_meme(prompt: str):
    response = client.images.generate(model=image_model,prompt=prompt,size=image_size,n=1,quality=image_quality)
    url = response.data[0].url
    return url

def generate_image_url(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
        image_url = f"data:image/jpeg;base64,{base64_image}"
        return image_url
    
def post_to_discord(image_url: str, text: str):
    url = st.secrets.requests.url1
    payload = {"text": text, "image": image_url}
    response = requests.post(url=url, json=payload)
    return response

image_path = "images/image2.png"
text = "Do you even trend, bro?"
image_url = generate_image_url(image_path=image_path)
response = post_to_discord(image_url=image_url, text=text)
print(response)