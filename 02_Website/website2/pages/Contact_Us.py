import streamlit as st
import email_mod
import pandas as pd

df = pd.read_csv('topics.csv')

st.header('Contact me')
with st.form(key='form_email', clear_on_submit=True):
    email = st.text_input('Your e-mail address')
    topic = st.selectbox('What topic do you want to discuss?', df['topic'])
    message = st.text_area('Your message')
    submit_button = st.form_submit_button()
    if submit_button:
        email_mod.send(email, topic, message)
        st.info('Your email was sent successfully.')
