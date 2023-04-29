import streamlit as st
from streamlit_option_menu import option_menu
from web_pages import home
from web_pages import contact_us


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    # initial_sidebar_state = "expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# # Hide a hamburger menu
# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

# sidebar menu
with st.sidebar:
    selected = option_menu("", ["Home", 'Contact Us!'],
                           icons=['house', 'person-lines-fill'], menu_icon="cast", default_index=0)

if selected == "Contact Us!":
    contact_us.show()
else:
    home.show()
