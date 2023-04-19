import tkinter as tk
from backend import TodoListController


class TodoList:
    def __init__(self, master):
        self.controller = TodoListController(self)
        self.listbox = tk.Listbox(master)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)

        self.entry = tk.Entry(self.button_frame)
        self.entry.pack()

        self.add_button = tk.Button(self.button_frame, text="Add Item", command=self.controller.add_item)
        self.add_button.pack(fill=tk.BOTH, pady=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Item", command=self.controller.edit_item)
        self.edit_button.pack(fill=tk.BOTH, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Item", command=self.controller.delete_item)
        self.delete_button.pack(fill=tk.BOTH, pady=5)

        self.controller.refresh_listbox()

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def get_selection(self):
        selection = self.listbox.curselection()
        if len(selection) > 0:
            return selection[0]
        else:
            return None

    def insert_item(self, item):
        self.listbox.insert(tk.END, item)

    def delete_item(self, index):
        self.listbox.delete(index)

    def update_item(self, index, item):
        self.listbox.delete(index)
        self.listbox.insert(index, item)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("To-Do List")
    view = TodoList(root)
    root.mainloop()
