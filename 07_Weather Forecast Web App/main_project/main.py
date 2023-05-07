import streamlit as st
import plotly.express as px
import backend

st.title('Weather Forecast for the Next Days')
city = st.text_input('City:')
days = st.slider('Forecast days:', min_value=1, max_value=5,
                 help='Select the numbers of forecasted days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {city}')

if city:
    data = backend.get_forecast(city, days)

    if data['cod'] == '200':

        dates = [x['dt_txt'] for x in data['list']]

        if option == 'Sky':
            filtered_data = [f"images/{x['weather'][0]['main'].lower()}.png" for x in data['list']]
            print(filtered_data)
            st.image(filtered_data, width=85)
        else:
            filtered_data = [x['main']['temp'] for x in data['list']]
            figure = px.line(x=dates, y=filtered_data, labels={'x': 'Date', 'y': 'Temperatures (°C)'})
            st.plotly_chart(figure)

    else:
        st.info(data['message'])
