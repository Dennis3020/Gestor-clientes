import helper as elp
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING
import database as db
class centerWindows:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.geometry(f"{w}x{h}+{x}+{y}")

class create(Toplevel, centerWindows):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear cliente")
        self.build()
        self.center()


    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        Label(frame, text="DNI (2 int y 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Nombre (2 a 20 char)").grid(row=0, column=1)
        Label(frame, text="Apellido (2 a 20 char)").grid(row=0, column=2)

        dni= Entry(frame)
        dni.grid(row=1, column= 0)
        dni.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        nombre= Entry(frame)
        nombre.grid(row=1, column= 1)
        nombre.bind("<KeyRelease>", lambda event:self.validate(event, 1))
        apellido= Entry(frame)
        apellido.grid(row=1, column= 2)
        apellido.bind("<KeyRelease>", lambda event:self.validate(event, 2))

        frame= Frame(self)
        frame.pack(pady= 10)
        crear= Button(frame, text="Crear", command=self.crearCliente)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text='Cancelar', command=self.close).grid(row=0, column=1)
        self.validacion = [0,0,0]
        self.crear= crear
        self.dni = dni
        self.nombre = nombre
        self.apellido= apellido

    def crearCliente(self):
        self.master.treeview.insert(
        parent='', index='end', iid=self.dni.get(),
        values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.crear(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()
    def validate(self, event, index):
        valor = event.widget.get()
        if index == 0:
            valido = elp.validacion_dni(valor, db.Clientes.lista)
            if valido:
                event.widget.configure({"bg": "Green"})
            else:event.widget.configure({"bg": "Red"})
        elif(index == 1):
            valido = valor.isalpha() and len(valor) >= 2 and len(valor) <= 20
            if valido:
                event.widget.configure({"bg": "Green"})
            else:event.widget.configure({"bg": "Red"})
        elif(index == 2):
            valido = valor.isalpha() and len(valor) >= 2 and len(valor) <= 20
            if valido:
                event.widget.configure({"bg": "Green"})
            else:event.widget.configure({"bg": "Red"})
        self.validacion[index] = valido
        self.crear.config(state=NORMAL if self.validacion == [1,1,1] else DISABLED)

class editar(Toplevel, centerWindows):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear cliente")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        Label(frame, text="DNI (No editable)").grid(row=0, column=0)
        Label(frame, text="Nombre (2 a 20 char)").grid(row=0, column=1)
        Label(frame, text="Apellido (2 a 20 char)").grid(row=0, column=2)

        dni= Entry(frame)
        dni.grid(row=1, column= 0)

        nombre= Entry(frame)
        nombre.grid(row=1, column= 1)
        nombre.bind("<KeyRelease>", lambda event:self.validate(event, 0))
        apellido= Entry(frame)
        apellido.grid(row=1, column= 2)
        apellido.bind("<KeyRelease>", lambda event:self.validate(event, 1))
        cliente = self.master.treeview.focus()
        campos = self.master.treeview.item(cliente, 'values')
        dni.insert(0, campos[0])
        dni.config(state=DISABLED)
        nombre.insert(0, campos[1])
        apellido.insert(0, campos[2])
        frame= Frame(self)
        frame.pack(pady= 10)
        Actualizar= Button(frame, text="Actualizar", command=self.editarCliente)
        Actualizar.grid(row=0, column=0)
        Button(frame, text='Cancelar', command=self.close).grid(row=0, column=1)
        self.validacion = [1,1]
        self.Actualizar= Actualizar
        self.dni = dni
        self.nombre = nombre
        self.apellido= apellido

    def editarCliente(self):
        cliente = self.master.treeview.focus()
        self.master.treeview.item(
        cliente, values=(self.dni.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.modificar(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.close()


    def close(self):
        self.destroy()
        self.update()
    def validate(self, event, index):
        valor = event.widget.get()
        if(index == 0):
            valido = valor.isalpha() and len(valor) >= 2 and len(valor) <= 20
            if valido:
                event.widget.configure({"bg": "Green"})
            else:event.widget.configure({"bg": "Red"})
        elif(index == 1):
            valido = valor.isalpha() and len(valor) >= 2 and len(valor) <= 20
            if valido:
                event.widget.configure({"bg": "Green"})
            else:event.widget.configure({"bg": "Red"})
        self.validacion[index] = valido
        self.Actualizar.config(state=NORMAL if self.validacion == [1,1] else DISABLED)




class MainWindows(Tk, centerWindows):
    def __init__(self):
        super().__init__()
        self.title('Gestor de clientes')
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()
        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI', 'Nombre', 'Apellido')
        treeview.column("#0", width= 0, stretch= NO)
        treeview.column("DNI", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Apellido", anchor=CENTER)

        treeview.heading('DNI', text= "DNI", anchor= CENTER)
        treeview.heading('Nombre', text= "Nombre", anchor= CENTER)
        treeview.heading('Apellido', text= "Apellido", anchor= CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        treeview['yscrollcommand'] = scrollbar.set
        for cliente in db.Clientes.lista:
            treeview.insert(
                parent="", index='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido))

        treeview.pack()
        frame = Frame(self)
        frame.pack(pady='20')
        Button(frame, text="Crear", command=self.creater).grid(row=1, column=0)
        Button(frame, text="Modificar", command=self.editat).grid(row=1, column=1)
        Button(frame, text="Borrar", command=self.delete).grid(row=1, column=2)

        self.treeview = treeview

    def delete(self):
        cliente= self.treeview.focus()
        if cliente:
            campos= self.treeview.item(cliente, 'values')
            confirmar = askokcancel(
                title= 'Confirmar borrado',
                message= f"¿Borrar a {campos[1]} {campos[2]}" ,
                icon= WARNING)
            if confirmar:
                self.treeview.delete(cliente)
                db.Clientes.borrar(campos[0])
    def creater(self):
        create(self)
    def editat(self):
        if self.treeview.focus():  editar(self)
if __name__ == '__main__':
    app= MainWindows()
    app.mainloop()
