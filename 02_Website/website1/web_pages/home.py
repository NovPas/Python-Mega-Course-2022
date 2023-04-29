import streamlit as st
import pandas as pd


def show():

    empty_col_1, col1, col2 = st.columns([.5, 1.5, 1.5])

    with col1:
        st.image('images/photo.jpg', width=200)

    with col2:
        st.title('Pavel Novozhilov')
        st.info('Some information about me.'
                )

    st.write("""
     Below you can find some of the apps I've built in Python.
     """)

    col3, empty_col_2, col4 = st.columns([1.5, .5, 1.5])

    df = pd.read_csv('data.csv', sep=';')

    with col3:
        for index, row in df.iloc[::2].iterrows():
            st.header(row['title'])
            st.write(row['description'])
            st.image('images/' + row['image'], width=300)
            st.write(f"[Source code]({row['url']})")

    with col4:
        for index, row in df.iloc[1::2].iterrows():
            st.header(row['title'])
            st.write(row['description'])
            st.image('images/' + row['image'], width=300)
            st.write(f"[Source code]({row['url']})")
