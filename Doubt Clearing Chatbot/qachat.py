from dotenv import load_dotenv
# loading all the environment variables
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai

# stored the api key in .env file with name "GOOGLE_API_KEY"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini model and get repsonses
model=genai.GenerativeModel('gemini-2.5-flash') # change model if this is outdated
chat = model.start_chat(history=[])

#defination to get response
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

#initializing streamlit app

st.set_page_config(page_title="Doubt Clearing Chatbot")

st.header("Doubt Clearing Chatbot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['Previous Doubt '] = []

input=st.text_input("Ask your Doubt: ",key="input")
submit=st.button("Get Solution")

#On clicking button
if submit and input:
    response=get_gemini_response(input)

    # Add user query and response to session state chat history
    st.session_state['Previous Doubt '].append((" You ", input))
    st.subheader("Solution : ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['Previous Doubt '].append(("Solution ", chunk.text))
st.subheader("Your Previous Doubts : ")
    
for role, text in st.session_state['Previous Doubt ']:
    st.write(f"{role}: {text}")
    



    

