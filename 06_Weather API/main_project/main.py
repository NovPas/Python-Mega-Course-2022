from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations_df = pd.read_csv('./data/stations.txt', usecols = ['STANAME                                 ','STAID'], skiprows=17)

@app.route('/')
def home():
    return render_template('home.html',  tables=[stations_df.to_html(classes='data')])

@app.route('/api/v1/<station>/<date>')
def get_temperature(station, date):
    stations_df.columns = stations_df.columns.str.replace(' ', '')
    stations_df['STANAME'] = stations_df['STANAME'].str.strip()
    result_df = stations_df.loc[stations_df['STANAME'] == station.upper()]
    if not result_df.empty:
        number_of_file = str(result_df.iloc[0]['STAID'])
        tg_staid_df = pd.read_csv(f'./data/TG_STAID{number_of_file.zfill(6)}.txt', skiprows=20)
        tg_staid_df.columns = tg_staid_df.columns.str.replace(' ', '')
        result_df = tg_staid_df.loc[tg_staid_df['DATE'] == int(date)]
        if not result_df.empty:
            tg = str(result_df.iloc[0]['TG']/10)
        else:
            tg = 'record not found'
    else:
        tg = 'station not found'
    return {'station': station, 'date': date, 'tempreture': tg}


@app.route('/api/v1/<station>')
def get_station_info(station):
    stations_df.columns = stations_df.columns.str.replace(' ', '')
    stations_df['STANAME'] = stations_df['STANAME'].str.strip()
    result_df = stations_df.loc[stations_df['STANAME'] == station.upper()]
    if not result_df.empty:
        number_of_file = str(result_df.iloc[0]['STAID'])
        tg_staid_df = pd.read_csv(f'./data/TG_STAID{number_of_file.zfill(6)}.txt', skiprows=20, usecols = ['    DATE','   TG'])
        tg_staid_df.columns = tg_staid_df.columns.str.replace(' ', '')
        return tg_staid_df.to_dict(orient='records')
    else:
        return 'data not found'


if __name__ == '__main__':
    app.run(debug=True)
