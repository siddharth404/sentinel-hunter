import streamlit as st
from PIL import Image
import exifread

def display_exif_analysis():
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg"])
    if uploaded_file:
        tags = exifread.process_file(uploaded_file)
        st.json({tag: str(value) for tag, value in tags.items() if "GPS" in tag})
