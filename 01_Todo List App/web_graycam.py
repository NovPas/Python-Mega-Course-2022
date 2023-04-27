# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image


def show_gray_image(image):
    if image:
        img = Image.open(image)
        gray_camera_img = img.convert('L')
        st.image(gray_camera_img)


st.subheader("Color to Grayscale Converter")

option_image = st.radio(
    "Choose a variant",
    ('Disk', 'Camera'))

if option_image == 'Disk':
    with st.expander("Upload Image"):
        image = st.file_uploader("Select Image", type=['png', 'jpg'])

else:
    with st.expander("Start camera"):
        image = st.camera_input("Camera")

show_gray_image(image)

# st.session_state
