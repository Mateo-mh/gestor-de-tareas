from tkinter import *
import sqlite3 # sqlite3 es un gestor de base de datos incluido en python

root = Tk()
root.title('Hola Mundo: todo list')
root.geometry('400x500')
root.configure(bg='#333233')

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

# Creando funcion remove para poder eliminar los todos
def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE id=?", (id, ))
        conn.commit()
        render_todos()
    return _remove
#-----------------------------

# Creando funcion de complete (currying(retrasamos la ejecución de una función) aplicado)
def complete(id):
    def _complete():
        todo = c.execute("SELECT * from todo WHERE id = ?", (id, )).fetchone() 
        c.execute("UPDATE todo SET completed = ? WHERE id = ?", (not todo[3], id))
        conn.commit()
        render_todos()
    return _complete
#-------------------------------

# Creando funcion para renderizar los elementos
def render_todos():
    rows = c.execute("SELECT * FROM todo").fetchall()
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        color = '#018CB1' if completed else '#555555'
        l = Checkbutton(frame, text=description, fg=color, width=42, anchor='w', command=complete(id))
        l.grid(row=i, column=0, sticky='w') # sticky 'w' pega la etiqueta a la izquierda
        btn = Button(frame, text='Eliminar', command=remove(id), bg='#018CB1', fg='white')
        btn.grid(row=i, column=1)       
        l.select() if completed else l.deselect()
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
l = Label(root, text='Tarea', fg='white', bg='#333233')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar', command=addTodo, fg='white', bg='#8A918C')
btn.grid(row=0, column=2)
#--------------------------------

# Creando el frame
frame = LabelFrame(root, text='Mis tareas', padx=5, pady=5, bg='#333233', fg='white')
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

e.focus()

root.bind('<Return>', lambda x: addTodo())
render_todos()
root.mainloop()