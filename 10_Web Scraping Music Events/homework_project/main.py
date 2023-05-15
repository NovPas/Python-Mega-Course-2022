import requests
from selectorlib import Extractor
# import csv
import time
# import os
from datetime import datetime
import sqlite3


URL = 'https://programmer100.pythonanywhere.com'
FILE_NAME = 'data.csv'

con = sqlite3.connect('data.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS weather(ts  timestamp, temperature)")

def scrape(url):
    """Scrape the web page from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['src']
    return value


def read_data():
    with open(FILE_NAME) as file:
        return file.read()


def save_data(extracted):
     # if not os.path.exists(FILE_NAME):
    #     with open(FILE_NAME, 'a', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(['date', 'temperature'])
    #
    # with open(FILE_NAME, 'a', newline='') as file:
    #     writer = csv.writer(file)
    #
    #     # write the header
    #     now = datetime.now()
    #     writer.writerow([now.strftime("%Y-%m-%d-%H-%M-%S"), extracted])
    cur.execute("INSERT INTO weather VALUES(?, ?)", (datetime.now(), extracted))
    con.commit()


if __name__ == '__main__':
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        save_data(extracted)
        time.sleep(1)