import tkinter as tk
from gui import TodoList

root = tk.Tk()
root.title("To-Do List")
view = TodoList(root)
root.mainloop()
