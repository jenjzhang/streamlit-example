from langchain.llms import OpenAI
import pandas as pd
import streamlit as st
import numpy as np
import os
import openai


# openai.api_key = os.environ['OPENAI_API_KEY']
openai.api_type = "azure"
openai.api_base = "https://ifopenairesourcedev.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "8edc50f1144c4fc380c90a493a17476e"


# Create functions
def generate_poem(topic, mood):
    '''Generate poem.'''
    prompt = f"Generate a poem about {topic} in a {mood} mood in less than 120 characters."

    completion = openai.ChatCompletion.create(
    engine="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    )
    st.info(completion.choices[0].message.content, icon="🤖")
        
# Configure Streamlit page and state
st.set_page_config(page_title="Poem", page_icon="✍️")

# Render Streamlit page
# streamlit_analytics.start_tracking()
st.title("JENerate Poems")
st.markdown(
    "This mini-app generates poems using the power of LLMs."
)


with st.form('my_form'):
    topic = st.text_input(label="Enter a topic, lyric, phrase to generate a poem upon:", placeholder="AI")
    mood = st.text_input(label="Enter a mood. Must be an adjective:", placeholder="inspirational")

    submitted = st.form_submit_button('Generate poem')

    if submitted:
        generate_poem(topic, mood)



# st.button(
#         label="Generate text",
#         type="primary",
#         on_click=generate_poem,
#         args=(topic,),
#     )

