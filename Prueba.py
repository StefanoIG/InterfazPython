import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess

#Propiedades de la ventana
LoginWindows=tk.Tk()
LoginWindows.title("Login")
LoginWindows.resizable(False,False)
LoginWindows.geometry("400x339")

# Conectar a la base de datos
conn = mysql.connector.connect(
    user="root",
    password='010304',
    host='localhost',
    database='Usuarios'
)

#Frame contenedor
container = tk.Frame(LoginWindows)
container.grid(sticky="nsew")

#Marco principal
MarcoPrincipal=tk.Frame(container)
MarcoPrincipal.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

#Etiquetas
Principal=Label(MarcoPrincipal,text="Iniciar Sesion",font=("Arial",24))
Principal.grid(row=0,column=0,columnspan=2,pady=10)

UsuarioLabel=Label(MarcoPrincipal,text="Usuario",font=("Arial",12))
UsuarioLabel.grid(row=1,column=0,padx=10,pady=10)

ContraLabel=Label(MarcoPrincipal,text="Contrasena",font=("Arial",12))
ContraLabel.grid(row=2,column=0,padx=10,pady=10)

#Entrys
InputUsuario=tk.Entry(MarcoPrincipal)
InputUsuario.grid(row=1,column=1,padx=10,pady=10)

InputContra=tk.Entry(MarcoPrincipal,show="*")
InputContra.grid(row=2,column=1,padx=10,pady=10)


#Funciones
def cerrar_ventana(event=None):
    conn.close()  # Cerrar la conexión
    LoginWindows.destroy()


def comprobar_datos():
    global conn  # Declarar la conexión como global para poder acceder a ella desde la función
    usuario = InputUsuario.get()
    contrasena = InputContra.get()

    # Consulta SQL para comprobar las credenciales
    consulta = f"SELECT * FROM ListadeEmpleados WHERE nombre='{usuario}' AND contrasena='{contrasena}'"

    # Ejecutar la consulta
    with conn.cursor() as cursor:
        cursor.execute(consulta)
        resultado = cursor.fetchone()

    if resultado is not None:
        tipo_prioridad = resultado[3]
        if tipo_prioridad == "alta":
            subprocess.call(["python", "Alta.py"])
            LoginWindows.destroy()
        elif tipo_prioridad == "media":
            subprocess.call(["python", "Media.py"])
            LoginWindows.destroy()
        elif tipo_prioridad == "baja":
            subprocess.call(["python", "Baja.py"])
        LoginWindows.destroy()

        return tipo_prioridad

    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        return None

LoginWindows.bind('<Escape>', cerrar_ventana)

#Botones
Login=tk.Button(MarcoPrincipal,text="Iniciar Sesion",font=("Arial",10),width=10, command=comprobar_datos)
Login.grid(row=6, column=1, pady=10, padx=10)


Salir=tk.Button(MarcoPrincipal,text="Salir",font=("Arial",10),width=10, command=cerrar_ventana)
Salir.grid(row=57,column=0,padx=10,pady=10)

#Centrar el contenedor
LoginWindows.grid_rowconfigure(0, weight=1)
LoginWindows.grid_columnconfigure(0, weight=1)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

#Iniciar la ventana
LoginWindows.mainloop()
