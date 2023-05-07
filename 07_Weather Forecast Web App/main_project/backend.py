import requests

APPID = '1186f8b884c838abd4df112a505e678a'


def get_forecast(city, days=1):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt={8*days}&APPID={APPID}'
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == '__main__':
    print(get_forecast('M', days=3))
