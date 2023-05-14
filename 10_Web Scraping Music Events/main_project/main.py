import requests
from selectorlib import Extractor
import email_mod
import time

URL = 'https://programmer100.pythonanywhere.com/tours/'
FILE_NAME = 'data.txt'


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
    with open(FILE_NAME, 'a') as file:
        file.write(extracted+'\n')


def send_email(extracted):
    email_mod.send('robot', 'New concerts', extracted)


if __name__ == '__main__':

    while True:

        time.sleep(5)

        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != 'No upcoming tours':
            content = read_data()
            if extracted not in content:
                save_data(extracted)
                send_email(extracted)
