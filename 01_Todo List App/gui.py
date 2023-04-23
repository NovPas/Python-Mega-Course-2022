import tkinter as tk
from tkinter import ttk
from backend import TodoListController


class TodoList:
    def __init__(self, master):
        self.master = master
        self.controller = TodoListController(self)
        self.listbox = tk.Listbox(master, height=3)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)

        self.img = tk.PhotoImage(file="switchtheme.png")
        self.theme_button = tk.Button(self.button_frame, image=self.img, bd=0, command=self.toggle_theme, width=20, height=10)
        self.theme_button.place(relx=1.0, x=-10, y=10, anchor="ne")
        self.theme_button.pack()

        self.entry = tk.Entry(self.button_frame)
        self.entry.pack()

        self.add_button = tk.Button(self.button_frame, text="Add Item", command=self.controller.add_item)
        self.add_button.pack(fill=tk.BOTH, pady=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Item", command=self.controller.edit_item)
        self.edit_button.pack(fill=tk.BOTH, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Item", command=self.controller.delete_item)
        self.delete_button.pack(fill=tk.BOTH, pady=5)

        self.theme = 'default'

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

    def on_select(self, event):
        # Get the selected value from the listbox
        selected_value = self.listbox.get(self.listbox.curselection())
        # Set the value of the entry field to the selected value
        self.entry.delete(0, tk.END)
        self.entry.insert(0, selected_value)

    def toggle_theme(self):
        if self.theme == 'default':
            self.theme_button.configure(text='Switch to Default Theme', fg='white')
            self.theme = 'dark'
            self.master.tk_setPalette(background='black', foreground='white')

        else:
            self.theme_button.configure(text='Switch to Dark Theme', fg='black')
            self.theme = 'default'
            self.master.tk_setPalette(background='white', foreground='black')


if __name__ == '__main__':
    root = tk.Tk()
    root.title("To-Do List")
    view = TodoList(root)
    root.mainloop()
