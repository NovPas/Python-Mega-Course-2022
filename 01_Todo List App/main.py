import os

def toDolistFunc():
    action = ''
    file_name = 'toDoList.txt'

    if os.path.isfile(file_name):
        with open(file_name) as f:
            toDoList = f.read().splitlines()
    else:
        toDoList = []

    while action != 'exit':

        action = input('show, add, delete, edit, save or exit: ')

        command = get_command(action)
        action = command['action']

        if action == 'show':
            print(*toDoList, sep="\n")
        elif action == 'add':
            toDoList.append(command['parameter'])
        elif action == 'delete':
            try:
                toDoList.remove(command['parameter'])
            except ValueError:
                pass  # do nothing!
        elif action == 'edit':
            try:
                i = toDoList.index(command['parameter'])
                newName = input('input a new name of the task: ')
                toDoList[i] = newName
            except ValueError:
                print("There's no element with this name")
        elif action == 'save':
            with open(file_name, 'w') as f:
                f.writelines(line + '\n' for line in toDoList)
        else:
            print('try again')


def get_command(string):
    all_words = string.split()
    first_word = all_words[0]
    other_words = string.replace(first_word, '', 1).strip()
    return {'action': first_word, 'parameter': other_words}


if __name__ == '__main__':
    toDolistFunc()
