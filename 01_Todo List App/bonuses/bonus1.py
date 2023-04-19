import random


lbound = input('Enter the lower bound: ')
hbound = input('Enter the higher bound: ')

print(random.randrange(int(lbound), int(hbound)+1))
