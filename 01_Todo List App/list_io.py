import os

FILE_NAME = 'toDoList.txt'


def read_list():
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME) as f:
            toDoList = f.read().splitlines()
    else:
        toDoList = []
    return toDoList


def save_list(toDoList):
    with open(FILE_NAME, 'w') as f:
        f.writelines(line + '\n' for line in toDoList)
