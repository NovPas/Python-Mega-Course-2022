# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image


def show_gray_image(image):
    if image:
        img = Image.open(image)
        gray_camera_img = img.convert('L')
        st.image(gray_camera_img)


st.subheader("Color to Grayscale Converter")

with st.expander("Upload Image"):
    uploaded_image = st.file_uploader("Select Image", type=['png', 'jpg'])

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

show_gray_image(uploaded_image)
show_gray_image(camera_image)

# st.session_state
