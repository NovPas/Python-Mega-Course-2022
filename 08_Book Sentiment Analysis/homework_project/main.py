import os
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
from datetime import datetime
import streamlit as st
import pandas as pd

subfolder = 'diary/'
list_data = []
analyzer = SentimentIntensityAnalyzer()

for filename in os.listdir(subfolder):
    date = filename.split('.')[0]
    with open(subfolder + filename, 'r', encoding='utf-8') as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    list_data.append(
        {'date': datetime.strptime(date, '%Y-%m-%d'), 'positivity': scores['pos'], 'negativity': scores['neg']})

df = pd.DataFrame(list_data)

st.title('Diary tone')
figure = px.line(data_frame=df, x='date', y='positivity', labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(figure)
figure = px.line(data_frame=df, x='date', y='negativity', labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(figure)
