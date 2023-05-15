import requests
from selectorlib import Extractor
import email_mod
import time
import sqlite3

URL = 'https://programmer100.pythonanywhere.com/tours/'
FILE_NAME = 'data.txt'

con = sqlite3.connect('./dbase/data1.db')
cur = con.cursor()

def scrape(url):
    """Scrape the web page from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['src']
    return value


def read_data(extracted):
    cond_list = extracted.split(',')
    cond_tuple = tuple(x.strip() for x in cond_list)
    res = cur.execute("SELECT 1 FROM events WHERE band=? AND city=? AND date=?", cond_tuple)
    row = res.fetchone()
    return row


def save_data(extracted):
    cond_list = extracted.split(',')
    cond_tuple = tuple(x.strip() for x in cond_list)
    cur.execute("INSERT INTO events VALUES(?, ?, ?)", cond_tuple)
    con.commit()  # Remember to commit the transaction after executing INSERT.


def send_email(extracted):
    email_mod.send('robot', 'New concerts', extracted)


if __name__ == '__main__':

    while True:

        time.sleep(1)

        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != 'No upcoming tours':
            content = read_data(extracted)
            if not content:
                save_data(extracted)
                send_email(extracted)
