from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
import streamlit as st
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input_text, image_data, user_prompt):
    response = model.generate_content(prompt=[input_text, image_data[0], user_prompt])
    return response.text

st.set_page_config("Image prompt generator")
st.header("BECOME A COMIC STAR !")

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{'mime_type': uploaded_file.type, 'data': bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError('No file uploaded')

st.header('Cartoon Comic Generator') #krish nayak on youtube

input_text = st.text_input('Input Prompt', key='input')
uploaded_file = st.file_uploader('Image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded File', use_column_width=True)

sub = st.button('Generate custom cartoon avatar')
input_prompt = """You are a cartoon artist. You will have to generate a cartoon avatar using the given image and text prompt from the user"""

if sub:
    with st.spinner('Wait'):
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input_text)
        st.subheader('The response is')
        st.text_area(label="", value=response, height=500)

  
