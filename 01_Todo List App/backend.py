import pickle


class TodoListController:
    def __init__(self, view):
        self.todo_list = []
        self.view = view
        self.load_list()

    def load_list(self):
        with open("todo_list.pkl", "rb") as file:
            self.todo_list = pickle.load(file)

    def save_list(self):
        with open("todo_list.pkl", "wb") as file:
            pickle.dump(self.todo_list, file)

    def refresh_listbox(self):
        self.view.listbox.delete(0, 'end')
        for item in self.todo_list:
            self.view.insert_item(item)

    def add_item(self):
        item = self.view.entry.get()
        if item:
            self.todo_list.append(item)
            self.view.insert_item(item)
            self.view.clear_entry()
            self.save_list()

    def edit_item(self):
        index = self.view.get_selection()
        if index is not None:
            item = self.view.entry.get()
            if item:
                self.todo_list[index] = item
                self.view.update_item(index, item)
                self.view.clear_entry()
                self.save_list()

    def delete_item(self):
        index = self.view.get_selection()
        if index is not None:
            self.todo_list.pop(index)
            self.view.delete_item(index)
            self.save_list()
