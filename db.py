from tkinter import *
import sqlite3 # sqlite3 es un gestor de base de datos incluido en python

root = Tk()
root.title('Hola Mundo: todo list')
root.geometry('350x500')

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

# Creando funcion para renderizar los elementos
def render_todos():
    rows = c.execute("SELECT * FROM todo").fetchall()
    print(rows)

    for i in range(0, len(rows)):
        completed = rows[i][3]
        description = rows[i][2]
        l = Checkbutton(frame, text=description, width=42, anchor='w')
        l.grid(row=i, column=0, sticky='w') # sticky 'w' pega la etiqueta a la izquierda
#----------------------------------
# Creando funcion para agregar tareas y que no se puedan agregar tareas vacias
def addTodo():
    todo = e.get()
    if todo:
        c.execute("""
            INSERT INTO todo (description, completed) VALUES (?, ?)
            """, (todo,False))
        conn.commit()
        e.delete(0, END)
        render_todos()
    else:
        pass
#--------------------------------

# Creando la interfaz grafica
l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar', command=addTodo)
btn.grid(row=0, column=2)
#--------------------------------

# Creando el frame
frame = LabelFrame(root, text='Mis tareas', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

e.focus()

root.bind('<Return>', lambda x: addTodo())
render_todos()
root.mainloop()