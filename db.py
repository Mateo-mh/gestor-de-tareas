from tkinter import *
import sqlite3 # sqlite3 es un gestor de base de datos incluido en python

root = Tk()
root.title('Hola Mundo: todo list')
root.geometry('500x500')

conn = sqlite3.connect('todo.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );  
""")

conn.commit()