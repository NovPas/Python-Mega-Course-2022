from tkinter import *
import tkinter.font as tkFont
from script_my_workWithBaseSQLite import *


def getStringForList(title, author, year, ISBN):
    return '%s, %s, %s, %s' % (title, author, year, ISBN)


def add_to_listbox(selected_tulip):
    title, author, year, ISBN = selected_tulip
    listbox1.insert(END, getStringForList(title, author, year, ISBN))


def btn_close_win():
    window.destroy()


def btn_add():

    insert(
        entry_title_value.get(),
        entry_author_value.get(),
        entry_year_value.get(),
        entry_ISBN_value.get())

    btn_viewAll()


def btn_search():
    rows = select(entry_title_value.get())
    if len(rows) > 0:
        title, author, year, ISBN = rows[0]
        entry_author_value.set(author)
        entry_year_value.set(year)
        entry_ISBN_value.set(ISBN)


def btn_viewAll():
    rows = view()
    listbox1.delete(0, END)
    [add_to_listbox(item) for item in rows]


def btn_delete():
    delete(entry_title_value.get())
    btn_viewAll()


def btn_update():
    update(
        entry_title_value.get(),
        entry_author_value.get(),
        entry_year_value.get(),
        entry_ISBN_value.get())

    btn_viewAll()


window = Tk()

window.geometry("1035x735")
window.configure(bg="#1f2320")
canvas = Canvas(
    window,
    bg="#1f2320",
    height=735,
    width=1035,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

myFont = tkFont.Font(size=30)

background_img = PhotoImage(
    file=f"script_my_workWithBaseUI_sources/background.png")
background = canvas.create_image(
    371.5, 118.5,
    image=background_img)

entry_img = PhotoImage(
    file=f"script_my_workWithBaseUI_sources/img_textBox.png")


# TITLE-----------------------------------------
entry_title_bg = canvas.create_image(
    268.0, 117.5,
    image=entry_img)

entry_title_value = StringVar()
entry_title = Entry(
    bd=0,
    bg="#888888",
    highlightthickness=0,
    textvariable=entry_title_value)

entry_title.place(
    x=64.0, y=73,
    width=408.0,
    height=87)

entry_title.configure(font=myFont)
# ----------------------------------------------


# AUTHOR----------------------------------------
entry_author_bg = canvas.create_image(
    764.0, 117.5,
    image=entry_img)

entry_author_value = StringVar()
entry_author = Entry(
    bd=0,
    bg="#888888",
    highlightthickness=0,
    textvariable=entry_author_value)

entry_author.place(
    x=560.0, y=73,
    width=408.0,
    height=87)

entry_author.configure(font=myFont)
# ----------------------------------------------


# YEAR---------------------------------------
entry_year_bg = canvas.create_image(
    268.0, 270.5,
    image=entry_img)

entry_year_value = StringVar()
entry_year = Entry(
    bd=0,
    bg="#888888",
    highlightthickness=0,
    textvariable=entry_year_value)

entry_year.place(
    x=64.0, y=226,
    width=408.0,
    height=87)

entry_year.configure(font=myFont)
# ----------------------------------------------


# ISBN---------------------------------------
entry_ISBN_bg = canvas.create_image(
    764.0, 270.5,
    image=entry_img)

entry_ISBN_value = StringVar()
entry_ISBN = Entry(
    bd=0,
    bg="#888888",
    highlightthickness=0,
    textvariable=entry_ISBN_value)

entry_ISBN.place(
    x=560.0, y=226,
    width=408.0,
    height=87)

entry_ISBN.configure(font=myFont)
# ----------------------------------------------


listbox1 = Listbox(
    # entry4 = Entry(
    bd=0,
    bg="#888888",
    highlightthickness=0)

listbox1.place(
    x=42, y=365,
    width=452,
    height=334)

listbox1.configure(font=myFont)

scrollbar = Scrollbar(listbox1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox1.config(yscrollcommand=scrollbar.set)

img0 = PhotoImage(file=f"script_my_workWithBaseUI_sources/img0.png")
btnClose = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_close_win,
    relief="flat")

btnClose.place(
    x=800, y=607,
    width=190,
    height=94)

img1 = PhotoImage(file=f"script_my_workWithBaseUI_sources/img1.png")

btnDelete = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_delete,
    relief="flat")

btnDelete.place(
    x=800, y=486,
    width=190,
    height=94)

img2 = PhotoImage(file=f"script_my_workWithBaseUI_sources/img2.png")
btn_update = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_update,
    relief="flat")

btn_update.place(
    x=800, y=365,
    width=190,
    height=94)

img3 = PhotoImage(file=f"script_my_workWithBaseUI_sources/img3.png")
btnAdd = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=btn_add,
    relief="flat")

btnAdd.place(
    x=574, y=607,
    width=190,
    height=94)

img4 = PhotoImage(file=f"script_my_workWithBaseUI_sources/img4.png")
btnSearch = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=btn_search,
    relief="flat")

btnSearch.place(
    x=574, y=486,
    width=190,
    height=94)

img5 = PhotoImage(file=f"script_my_workWithBaseUI_sources/img5.png")
btnViewAll = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=btn_viewAll,
    relief="flat")

btnViewAll.place(
    x=574, y=365,
    width=190,
    height=94)

window.resizable(False, False)

btn_viewAll()

window.mainloop()
