from list_io import read_list, save_list


def todo_list_func():
    action = ''

    toDoList = read_list()

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
            save_list(toDoList)
        else:
            print('try again')


def get_command(string):
    all_words = string.split()
    first_word = all_words[0]
    other_words = string.replace(first_word, '', 1).strip()
    return {'action': first_word, 'parameter': other_words}


if __name__ == '__main__':
    todo_list_func()
