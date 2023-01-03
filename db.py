from tkinter import *
import sqlite3 # sqlite3 es un gestor de base de datos incluido en python

root = Tk()
root.title('Hola Mundo: todo list')
root.geometry('500x500')

# Crear y conectar base de datos
conn = sqlite3.connect('todo.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );  
""")

conn.commit()
# -------------------------------

# Creando la interfaz grafica
l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar')
btn.grid(row=0, column=2)

# Creando el frame
frame = LabelFrame(root, text='Mis tareas', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

root.mainloop()