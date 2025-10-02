# generate infomation from/of image
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai

# stored the api key in .env file with name "GOOGLE_API_KEY"
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-2.5-flash') # change model if this is outdated
    if input!="":   
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

# initializing streamlit app

st.set_page_config(page_title="My Gemini Image App")

st.header("Ask Via Image")
input=st.text_input("Ask Anything: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit=st.button("Get Response")

# If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is:")
    st.write(response)
