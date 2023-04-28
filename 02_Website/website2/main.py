import streamlit as st
import pandas as pd


def fill_column(col, df_needable):
    with col:
        for index, row in df_needable:
            fn = row["first name"].capitalize()
            ln = row["last name"].capitalize()
            st.header(fn+' '+ln)
            st.write(row['role'])
            st.image('images/' + row['image'], width=200)


st.set_page_config(
    page_title="The best company App",
    page_icon=":random:",
    layout="wide"
  )

st.title('The best company')
st.info("""NovPasCo is a leading IT company specializing in developing cutting-edge software solutions for businesses
 of all sizes. With a team of highly skilled developers and designers, NovPasCo offers customized software development,
 cloud computing services, and AI-powered solutions to help businesses streamline their operations and boost productivity.""")

st.subheader('Our team')

col1, col2, col3 = st.columns(3)

df = pd.read_csv('data.csv')

fill_column(col1, df.iloc[::3].iterrows())
fill_column(col2, df.iloc[1::3].iterrows())
fill_column(col3, df.iloc[2::3].iterrows())