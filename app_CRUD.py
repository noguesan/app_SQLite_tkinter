"""
Esta es una aplicacion grafica para usos base de datos de una forma facil.
Crea una base de datos o usa la ya existente y hace las funciones basicas de CRUD (creado, lectura, actualizado y borrado de datos).
Para la interfaz grafica utiliza la libreria tkinter y para la base de datos utiliza la libreria sqlite3
"""






#IMPORTACION LIBRERIAS

from tkinter import *
from tkinter import messagebox
import sqlite3
from matplotlib.pyplot import text
from sklearn.cluster import mean_shift
from sqlalchemy import column

#---------------------------------------------------------------------------------------
#------------------------------funciones
def conexionBBDD():

    miConexion = sqlite3.connect("Gestion_usuarios") 
    miCursor=miConexion.cursor()

#Crear tabla
    try:

        miCursor.execute('''
            CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(30),
            APELLIDO VARCHAR(30),
            DIRECCION VARCHAR(50),
            PASSWORD VARCHAR(50),
            COMENTARIOS VARCHAR(100))
        ''')

        messagebox.showinfo("BBDD", "BBDD creada con éxito")

    except:

        messagebox.showwarning("Atención", "La BBDD ya existe")


# --------
def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        raiz.destroy()    

# --------

def limpiarCampos():
    """
    Es la funcion del boton de borrar que pone todas las cosas como al inicio (borra el contenido de todo)
    """
    miID.set("")
    minombre.set("")
    miapellido.set("")
    micontrasena.set("")
    midireccion.set("")
    comentarioText.delete('1.0', END)

# --------
def crear():
    miConexion = sqlite3.connect("Gestion_usuarios") 
    miCursor=miConexion.cursor()

    #opcion 1
    # miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES (NULL, '" + minombre.get() + 
    #     "','" + miapellido.get()+
    #     "','" + micontrasena.get()+
    #     "','" + midireccion.get()+
    #     "','" + comentarioText.get("1.0", END) + "')")

    #opcion 2
    sql = "INSERT INTO DATOS_USUARIOS VALUES (NULL,?,?,?,?,?)"
    usuario_agregado =minombre.get(), miapellido.get(),micontrasena.get(),midireccion.get(),comentarioText.get("1.0", END)
    miConexion.execute(sql,usuario_agregado)



    miConexion.commit()
    
    messagebox.showinfo("BBDD", "Regiostro insertado con éxito")
    #se podria agregar un mensaje para cuando no funciona

    # --------
def leer():
    miConexion = sqlite3.connect("Gestion_usuarios") 
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID="+ miID.get())
    elUsuario = miCursor.fetchall()

    for usuario in elUsuario:
        miID.set(usuario[0])
        minombre.set(usuario[1])
        miapellido.set(usuario[2])
        micontrasena.set(usuario[3])
        midireccion.set(usuario[4])
        comentarioText.insert(1.0,usuario[5])

    miConexion.commit()

# --------
def actualizar():
    miConexion = sqlite3.connect("Gestion_usuarios") 
    miCursor=miConexion.cursor()

    # #opcion 1
    # miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE='"+ minombre.get() + 
    #     "', APELLIDO='" + miapellido.get()+
    #     "', DIRECCION='" + micontrasena.get()+
    #     "', PASSWORD='" + midireccion.get()+
    #     "', COMENTARIOS='" + comentarioText.get("1.0", END) + 
    #     "' WHERE ID=" + miID.get())

    #opcion 2
    sql = "UPDATE DATOS_USUARIOS SET NOMBRE=?, APELLIDO=?, DIRECCION=?, PASSWORD=?, COMENTARIOS=? WHERE ID=?"
    usuario_actualizado=minombre.get(), miapellido.get(),micontrasena.get(),midireccion.get(),comentarioText.get("1.0", END), miID.get()
    miConexion.execute(sql,usuario_actualizado)

    miConexion.commit()
    
    messagebox.showinfo("BBDD", "Regiostro actualizado con éxito")    

# --------
def eliminar():
    
    miConexion = sqlite3.connect("Gestion_usuarios") 
    miCursor=miConexion.cursor()

    miCursor("DELETE FROM DATOS_USUARIOS WHERE ID=" + miID.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Regiostro borrado con éxito")

# --------
def infoAdicional():
    """
    Abre una ventana de informacion, cuando se ingresa a Barra de menu/Ayuda/Acerca de ..
    """
    messagebox.showinfo("Procesador de Santi", "app CRUD 1.0")

def avisoLicencia():
    """
    Abre una ventana de aviso, cuando se ingresa a Barra de menu/Ayuda/Licencia
    """
    messagebox.showwarning("Licencia", "Producto bajo licencia xxxxx")
#---------------------------------------------------------------------------------------
#------------------------------VENTANA PRINCIPAL
raiz = Tk()
raiz.title("Intefas grafica CRUD")

#---------------------------------------------------------------------------------------
#--------------------------VENTANA GRAFICA - BARRA MENU

#variable para el menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

#---------------------------------------------------------------------------------------------------
# ASIGNACION ELEMENTOS A LA BARRA DE MENU

bbddMenu = Menu(barraMenu, tearoff=0)
#tearoff es para sacar el "regloncito de guiones" (paracido al separator) que aparece cuando abris el menu
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear (Create)", command=crear)
crudMenu.add_command(label="Leer (Read)", command=leer)
crudMenu.add_command(label="Actualizar (Update)", command= actualizar)
crudMenu.add_command(label="Borrar (Delete)")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de..", command=infoAdicional)


#---------------------------------------------------------------------------------------------------
# NOMBRES DE LOS ELEMENTOS DEL MENU
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)




#---------------------------------------------------------------------------------------
#------------------------------------------CAMPOS---------------------------------------  

#---------------------------------------------------------------------------------------
# FRAMES PARA ORDENAR EL ESPACIO DE LA VENTANA
miFrame1=Frame(raiz, width=1200, height=600)
miFrame1.pack(fill='both', expand = 'True', side = "top")

botonesFrame=Frame(raiz, width=1200, height=600)
botonesFrame.pack(fill='both', expand = 'True', side = "top")

#---------------------------------------------------------------------------------------
#DEFINICION VARIABLES

# Variables de los entrys
miID=StringVar()
minombre = StringVar()
miapellido = StringVar()
micontrasena = StringVar()
midireccion = StringVar()
micomentario = StringVar()


#---------------------------------------------------------------------------------------
# ENTRADAS PARA INTRODUCIR TEXTO
IDEntry = Entry(miFrame1, textvariable=miID)
IDEntry.grid(row=0, column=1, padx=10, pady=10)

nombreEntry = Entry(miFrame1, textvariable=minombre)
nombreEntry.grid(row=1, column=1, padx=10, pady=10)
nombreEntry.config(fg="red", justify="center")

apellidoEntry = Entry(miFrame1, textvariable=miapellido)
apellidoEntry.grid(row=2, column=1, padx=10, pady=10)

direccionEntry = Entry(miFrame1, textvariable=midireccion)
direccionEntry.grid(row=3, column=1, padx=10, pady=10)

contrasenaEntry = Entry(miFrame1, textvariable=micontrasena)
contrasenaEntry.grid(row=4, column=1, padx=10, pady=10)
contrasenaEntry.config(show="*")
#show: es para mostrar lo que se asigne en lugar de lo que se escribe

#---------------------------------------------------------------------------------------
# LABELS AL COSTADO IZQUIERDO DE LAS ENTRADAS O TEXTOS SEGUN CORRESPONDA

nombreLabel=Label(miFrame1, text="ID: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) 
#Sticky es para oriental el label y que quede pegado en la direccion este

nombreLabel=Label(miFrame1, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) 

apellidoLabel=Label(miFrame1, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame1, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

contrasenaLabel=Label(miFrame1, text="Password:")
contrasenaLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

contrasenaLabel=Label(miFrame1, text="Comentarios:")
contrasenaLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#---------------------------------------------------------------------------------------
#TEXTO, PARA LA INTRODUCION DE TEXTOS "LARGOS"

comentarioText = Text(miFrame1, width=16, height=5)
comentarioText.grid(row=5, column=1, padx=10, pady=10)

#scrollbar asociado al texto
scrollVert=Scrollbar(miFrame1, command=comentarioText.yview)
scrollVert.grid(row=5, column=2, sticky= "nsew")
#nsew: le da un tamano mas "amigable" al Scrollbar
comentarioText.config(yscrollcommand=scrollVert.set) #"asocia el tamano" del Texto al ScrolVert




#---------------------------------------------------------------------------------------
#BOTONES

botonCrear=Button(botonesFrame, text = "Create", command=crear) 
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)


botonLeer=Button(botonesFrame, text = "Read", command=leer) 
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(botonesFrame, text = "Update", command= actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(botonesFrame, text = "Delete") #, command=codigoBoton)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


#---------------------------------------------------------------------------------------
# VISUALIZACION VENTANA GRAFICA
raiz.mainloop()