import requests
from selectorlib import Extractor
import email_mod
import time
import sqlite3

URL = 'https://programmer100.pythonanywhere.com/tours/'
# FILE_NAME = 'data.txt'


class Events:
    def scrape(self, url):
        """Scrape the web page from the URL"""
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        extractor = Extractor.from_yaml_file('extract.yaml')
        value = extractor.extract(source)['src']
        return value


class Dbase:

    def __init__(self, database_path):
        self.con = sqlite3.connect(database_path)
        self.cur = self.con.cursor()

    def read_data(self, extracted):
        cond_list = extracted.split(',')
        cond_tuple = tuple(x.strip() for x in cond_list)
        res = self.cur.execute("SELECT 1 FROM events WHERE band=? AND city=? AND date=?", cond_tuple)
        row = res.fetchone()
        return row

    def save_data(self, extracted):
        cond_list = extracted.split(',')
        cond_tuple = tuple(x.strip() for x in cond_list)
        self.cur.execute("INSERT INTO events VALUES(?, ?, ?)", cond_tuple)
        self.con.commit()  # Remember to commit the transaction after executing INSERT.


class Email:
    def send(self, extracted):
        email_mod.send('robot', 'New concerts', extracted)


if __name__ == '__main__':

    event = Events()
    email = Email()
    dbase = Dbase(database_path='./dbase/data1.db')

    while True:

        time.sleep(1)

        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != 'No upcoming tours':
            content = dbase.read_data(extracted)
            if not content:
                dbase.save_data(extracted)
                email.send(extracted)
