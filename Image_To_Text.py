import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.json()

st.title("Image Captioning App")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type="jpg")

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Button to generate caption
    if st.button("Convert to Text"):
        # Convert image to text
        image_bytes = uploaded_file.read()  # Correctly read the uploaded file as bytes
        output = query(image_bytes)
        
        # Display the output
        st.write("Generated Caption:")
        st.write(output[0]['generated_text'])
