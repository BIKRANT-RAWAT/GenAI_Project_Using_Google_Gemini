from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer
import streamlit as st

# Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

# starting the task execution process wiht enhanced feedback


# initializing streamlit app

st.set_page_config(page_title=" Question & Answer Model")

st.header("Welcome to Question and Answer Chat")

input=st.text_input("Ask Anything : ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    result=crew.kickoff(inputs={'topic':{input}})
    st.subheader("Answer:")
    st.write(result)