import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv('happy.csv')
st.title('In search for happiness')
optionsX = st.selectbox('Select the data for the X-axis', tuple(df.columns))
optionsY = st.selectbox('Select the data for the Y-axis', tuple(df.columns))
st.subheader(f'{optionsX} and {optionsY}')

dataX = list(df[optionsX])
dataY = list(df[optionsY])

# figure = px.scatter(x=dataX, y=dataY)
figure = px.scatter(df, x=optionsX, y=optionsY)
st.plotly_chart(figure)
