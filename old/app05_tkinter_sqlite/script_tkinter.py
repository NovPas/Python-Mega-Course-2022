from tkinter import *

def km_to_miles():
    miles  = float(e1_value.get())*1.6
    t1.delete("1.0", END)
    t1.insert(END, miles)

window = Tk()
window.geometry("300x300")

b1 = Button(window, text = 'push me', command=km_to_miles)
b1.grid(row=1, column=1)

e1_value = StringVar()
e1 = Entry(window, text='entry', textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=2, width=20)
t1.grid(row=0, column=2)


window.mainloop()