import os
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import requests
import google.generativeai as genai
import io

# Load environment variables from the .env file
load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.getenv("AIzaSyADox2adxHidZX_87tntJ8YSBKFYvt1oHA"))

# Initialize the app
st.set_page_config(page_title="LLM Project")
st.header("LLM Gemini Application Project")

# Input field for the user to ask a question
user_question = st.text_input("Ask something", key="input")

# File uploader for image
uploaded_file = st.file_uploader("Upload an image (optional)", type=['jpg', 'jpeg', 'png'])

# Submit button
submit = st.button("Submit")

def get_gemini_model_response(question, image=None):
    model = genai.GenerativeModel("gemini-pro")  # Use the appropriate model name
    
    # Create request data
    data = {"question": question}
    files = {}
    
    if image:
        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=image.format)
        img_byte_arr = img_byte_arr.getvalue()
        files = {
            'image': ('image.jpg', img_byte_arr, 'image/jpeg')
        }
    
    # Make the request to the Gemini API
    response = requests.post(
        "https://ai.google.dev/gemini-api/docs/api-key",  # Replace with the actual API endpoint
        headers={"Authorization": f"Bearer {os.getenv('GOOGLE_API_KEY')}", "Content-Type": "application/json"},
        data=data,
        files=files
    )
    
    if response.status_code == 200:
        return response.json().get("answer", "No answer returned by the API.")
    else:
        return f"Error: {response.status_code}, {response.text}"

if submit:
    image = None
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if user_question:
        model_response = get_gemini_model_response(user_question, image)
        st.write(model_response)
    else:
        st.write("Please enter a question.")
