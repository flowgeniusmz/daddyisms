import streamlit as st
from openai import OpenAI
from generate_image import generate_meme
from generate_text import generate_text

container1 = st.container(border=False)
st.divider()
container2 = st.container(border=False)
st.divider()
container3 = st.container(border=False)

with container1:
    st.title("Create Daddyism")
