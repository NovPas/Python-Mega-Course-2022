import sqlite3

def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER, ISBN TEXT)")
    conn.commit()
    conn.close()


def insert(title, author, year, ISBN):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (?,?,?,?)", (title, author, year, ISBN))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    return rows


def select(title):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? LIMIT 1", (title,))
    rows = cur.fetchall()
    return rows


def update(title, author, year, ISBN):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET author=?, year=?, ISBN=? WHERE title=?",
                (author, year, ISBN, title))
    conn.commit()
    conn.close()


def delete(title):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE title=?", (title,))
    conn.commit()
    conn.close()

create_table()