import streamlit as st


def show():
    st.header('Contact me')
    with st.form(key='form_email'):
        email = st.text_input('Your e-mail address')
        message = st.text_area('Your message')
        submit_button = st.form_submit_button()
        if submit_button:
            print('hi')
