import streamlit as st
from openai import OpenAI
from initial_messages import initialmessages

client = OpenAI(api_key=st.secrets.openai.api_key)
model = "gpt-4o"
input = initialmessages
tools = [{"type": "web_search_preview"}]

def generate_text():
    response = client.responses.create(
        model=model,
        input=input,
        tools=tools,
        temperature=1,
        max_output_tokens=2048,
        top_p=1,
        store=True
    )
    output = response.output_text
    return output

a = create_daddyism()
print(a)