import requests
from bs4 import BeautifulSoup
import email_mod
from datetime import datetime, timedelta

current_date = datetime.today().date()
date = current_date - timedelta(days=1)
formatted_date = date.strftime('%Y/%m/%d')
url = f'https://www.mk.ru/editions/daily/{formatted_date}/goryachaya-pyaterka-anekdotov-mk.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('p')
result = soup.find('div', {'class': 'article__body', 'itemprop': 'articleBody'})

email_mod.send('Anecdot', f'Anecdots of {current_date}', result.text)

