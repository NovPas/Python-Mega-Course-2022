import streamlit as st
import email_mod


def show():
    st.header('Contact me')
    with st.form(key='form_email', clear_on_submit=True):
        email = st.text_input('Your e-mail address')
        message = st.text_area('Your message')
        submit_button = st.form_submit_button()
        if submit_button:
            email_mod.send(email, message)
            st.info('Your email was sent successfully.')