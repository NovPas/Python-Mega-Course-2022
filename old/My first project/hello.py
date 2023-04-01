import os
import pandas
import time

fileName = 'temps_today.csv'

while True:

    if os.path.exists(fileName):
        data = pandas.read_csv(fileName)
        print(data.mean()['st1'])
    else:
        print('not exist')
    
    time.sleep(1)