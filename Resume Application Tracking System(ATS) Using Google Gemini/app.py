#Resume Application Tracking System(ATS) Using Google Gemini

#for .env file where api key is loaded
from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image        #install poppler-windows is important
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#to get Gemini reponse 
def get_gemini_response(input,pdf_cotent,prompt):
    model=genai.GenerativeModel('gemini-2.5-flash')  # change model as per use case
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    """
    Convert the first page of a PDF into a JPEG image and return as base64.
    Requires Poppler installed and accessible via the given poppler_path.
    download Poppler https://github.com/oschwartz10612/poppler-windows/releases/
    """
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded.")

    try:
        # Convert PDF to images using Poppler
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(),
            poppler_path=r"C:\poppler-25.07.0\Library\bin"
        )

        if not images:
            raise ValueError("No pages found in PDF.")

        # Take the first page
        first_page = images[0]

        # Convert page to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_bytes = img_byte_arr.getvalue()

        # Encode to base64
        pdf_parts = [{
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_bytes).decode()
        }]

        return pdf_parts

    except Exception as e:
        raise RuntimeError(f"Error while processing PDF: {e}")

#Setting up Streamlit 

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("Percentage match and requirements")

#Discribing Role
input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of domain knownledge and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. Also give output whether this resume will qualify with ATS or not. First the output should come as percentage and then qualification then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



   





