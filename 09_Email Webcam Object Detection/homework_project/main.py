import cv2
import streamlit as st
from datetime import datetime


st.title('Motion detections')
start = st.button('Start camera')

if start:
    camera = cv2.VideoCapture(0)
    streamlit_image = st.image([])

    # get current datetime
    week_day = datetime.now().strftime('%A')

    while True:
        check, frame = camera.read()
        frame =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(img=frame, text=week_day, org=(10,30), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255,255,255))
        current_time = datetime.now().strftime("%H:%M:%S")
        cv2.putText(img=frame, text=current_time, org=(20,50), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=1.5, color=(0,255,0))
        streamlit_image.image(frame)