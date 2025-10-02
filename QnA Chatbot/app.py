# Q&A Chatbot

#create .env file and store api key in that file
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY") # saved api in "GOOGLE_API_KEY"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini pro model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-2.5-flash')  # change model as per use case
    response = model.generate_content(question)  # response stored from the model
    return response.text

# initializing streamlit app

st.set_page_config(page_title=" Question & Answer Model")

st.header("Welcome to Question and Answer Chat")

input=st.text_input("Ask Anything : ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("Answer : ")
    st.write(response)
