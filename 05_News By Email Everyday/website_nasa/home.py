import streamlit as st
import requests

url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
r = requests.get(url)
rjson = r.json()

st.image(rjson['url'], width=400)
st.info(rjson['explanation'])
