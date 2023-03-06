import tkinter as tk
from tkinter import *
import subprocess
import mysql.connector

# Propiedades de la ventana
MainVentana = tk.Tk()
MainVentana.title("Interfaz de prioridad alta")
MainVentana.resizable(False, False)
MainVentana.attributes("-fullscreen", True)

# Frames
FrameEncabezado = tk.Frame(MainVentana)
FrameEncabezado.grid(row=0, column=0, sticky="nsew")
FrameCuerpo = tk.Frame(MainVentana)
FrameCuerpo.grid(row=1, column=0, sticky="nsew")

# Agregar padding a los frames
FrameEncabezado.grid_rowconfigure(0, weight=1)
FrameEncabezado.grid_columnconfigure(0, weight=1)
FrameCuerpo.grid_rowconfigure(0, weight=1)
FrameCuerpo.grid_columnconfigure(0, weight=1)

# Frames secundarios
FrameCuerpo_resumen = tk.Frame(FrameCuerpo, borderwidth=1, relief="groove", highlightthickness=1)
FrameCuerpo_inventario = tk.Frame(FrameCuerpo, borderwidth=1, relief="groove", highlightthickness=1)
FrameCuerpo_empleados = tk.Frame(FrameCuerpo, borderwidth=1, relief="groove", highlightthickness=1)
FrameCuerpo_clientesventas = tk.Frame(FrameCuerpo, borderwidth=1, relief="groove", highlightthickness=1)
FrameCuerpo_comunicacion = tk.Frame(FrameCuerpo, borderwidth=1, relief="groove", highlightthickness=1)

# Definir columnas y filas para cada frame
FrameCuerpo_resumen.grid_columnconfigure(0, weight=1)
FrameCuerpo_resumen.grid_rowconfigure(0, weight=1)
FrameCuerpo_resumen.grid_rowconfigure(1, weight=1)

FrameCuerpo_inventario.grid_columnconfigure(0, weight=1)
FrameCuerpo_inventario.grid_rowconfigure(0, weight=1)

FrameCuerpo_empleados.grid_columnconfigure(0, weight=1)
FrameCuerpo_empleados.grid_rowconfigure(0, weight=1)

FrameCuerpo_clientesventas.grid_columnconfigure(0, weight=1)
FrameCuerpo_clientesventas.grid_rowconfigure(0, weight=1)

FrameCuerpo_comunicacion.grid_columnconfigure(0, weight=1)
FrameCuerpo_comunicacion.grid_rowconfigure(0, weight=1)

# Iniciar Frames
FrameCuerpo_comunicacion.grid(sticky="nsew", column=4, row=4, rowspan=20)
FrameCuerpo_clientesventas.grid(sticky="nsew", column=3, row=3, rowspan=20)
FrameCuerpo_inventario.grid(sticky="nsew", column=1, row=1, rowspan=20)
FrameCuerpo_resumen.grid(sticky="nsew", column=0, row=0, rowspan=20)

# Funciones de los widgets
imagen = PhotoImage(file="logo.png")

# Definir el tamaño máximo deseado
maximo_tamano = 150

# Obtener las medidas
ancho_original = imagen.width()
alto_original = imagen.height()

# Calcular el factor de reducción necesario para ajustar la imagen al tamaño máximo
factor_reduccion = max(ancho_original, alto_original) / maximo_tamano

#Si el factor de reducción es mayor que 1, reducir la imagen
if factor_reduccion>1:
    ancho_reducido = int(ancho_original / factor_reduccion)
    alto_reducido = int(alto_original / factor_reduccion)
    imagen_reducida = imagen.subsample(int(factor_reduccion))
    imagen_reducida.config(width=ancho_reducido, height=alto_reducido)
#si la imagen es adecuada
else:
    imagen_reducida=imagen

#Crear el label con la imagen reducida
Resumen = Label(FrameCuerpo_resumen, image=imagen_reducida)
Resumen.grid(rowspan=10, row=1, column=1,sticky="nsew")




#Barra de menú
menubar = tk.Menu(MainVentana)

# Menú de archivo
filemenu = tk.Menu(menubar, tearoff=0)

# Submenú para la opción "Nuevo"
newsubmenu = tk.Menu(filemenu, tearoff=0)
newsubmenu.add_command(label="Opción 1")
newsubmenu.add_command(label="Opción 2")
newsubmenu.add_command(label="Opción 3")

filemenu.add_command(label="Abrir")
filemenu.add_cascade(label="Nuevo", menu=newsubmenu)  # Agregar el submenú
filemenu.add_command(label="Guardar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=MainVentana.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

# Menú de ayuda
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_command(label="Acerca de")
menubar.add_cascade(label="Ayuda", menu=helpmenu)

#Widgets de version alta
Resumen=tk.Label(FrameCuerpo_resumen,text="Resumen de ventas")
InformacionInventario=tk.Label(FrameCuerpo_inventario,text="Inventario")
GesEmpleados=tk.Label(FrameCuerpo_empleados,text="Empleados")
GesClientes=tk.Label(FrameCuerpo_clientesventas,text="Clientes y ventas")
Comunicacion=tk.Label(FrameCuerpo_comunicacion,text="Comunicacion")

Resumen.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
InformacionInventario.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
GesEmpleados.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
GesClientes.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
Comunicacion.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

#Centrar los widgets en los respectivos frames
FrameCuerpo_resumen.columnconfigure(0, weight=1)
FrameCuerpo_resumen.rowconfigure(0, weight=1)
FrameCuerpo_inventario.columnconfigure(0, weight=1)
FrameCuerpo_inventario.rowconfigure(0, weight=1)
FrameCuerpo_empleados.columnconfigure(0, weight=1)
FrameCuerpo_empleados.rowconfigure(0, weight=1)
FrameCuerpo_clientesventas.columnconfigure(0, weight=1)
FrameCuerpo_clientesventas.rowconfigure(0, weight=1)
FrameCuerpo_comunicacion.columnconfigure(0, weight=1)
FrameCuerpo_comunicacion.rowconfigure(0, weight=1)


#Centrar los FramesPrincipales
MainVentana.grid_rowconfigure(1, weight=1)
MainVentana.grid_columnconfigure(0, weight=1)
FrameEncabezado.grid(row=0, column=0, sticky="nsew")
FrameCuerpo.grid(row=1, column=0, sticky="nsew")


MainVentana.config(menu=menubar)

MainVentana.mainloop()
