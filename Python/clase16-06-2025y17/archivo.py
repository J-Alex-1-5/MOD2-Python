import tkinter as tk   # Importar la librería tkinter
from tkinter import filedialog # Importar filedialog para abrir y guardar archivos

#Funcioens Call Back
def nuevo_archivo():
    areaTexto.delete(1.0,tk.END)

# Función para abrir un archivo
def abrir_archivo():
    global rutaArchivo
    rutaArchivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt"),("Archivos de Python", "*.py"),("Todos los archivos", "*.*")])
    
    with open(rutaArchivo, "r", encoding="utf-8") as file:
        areaTexto.insert(tk.INSERT, file.read())
    print(rutaArchivo)

# Función para guardar el archivo actual
def guardar_archivo():
    global rutaArchivo
    if rutaArchivo:
        try:
            with open(rutaArchivo,"w",encoding="utf-8") as file:
                file.write(areaTexto.get(1.0,tk.END))
        except:
            print("No se pudo guardar el documento")

# Función para guardar el archivo con un nuevo nombre
def guardar_como():
    nuevaRuta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt"),("Archivos de Python", "*.py"),("Todos los archivos", "*.*")])

    if nuevaRuta:
        with open(nuevaRuta, "w",encoding="utf-8") as file:
            file.write(areaTexto.get(1.0,tk.END))
        
    print(nuevaRuta)

# Funciones para copiar, pegar y cortar texto
def copiar():
    areaTexto.event_generate(("<<Copy>>"))

# Función para pegar texto desde el portapapeles
def pegar():
    areaTexto.event_generate(("<<Paste>>"))

# Función para cortar texto seleccionado
def cortar():
    areaTexto.event_generate(("<<Cut>>"))

# Crear la ventana principal
ventana = tk.Tk() # Crear una instancia de Tk
ventana.iconbitmap("icono.ico") # Cambiar el icono de la ventana
ventana.title("Bloc de Notas")# Establecer el título de la ventana
ventana.geometry("800x600") # Establecer el tamaño de la ventana
rutaArchivo = ""
menu = tk.Menu(ventana) # Crear un menú
ventana.config(menu=menu) # Configurar el menú en la ventana

# Crear los submenús de Archivo y Edición
archivo = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo)

# Submenú de Archivo
edicion = tk.Menu(menu)
menu.add_cascade(label="Edicion", menu=edicion)

# Crear un área de texto para el bloc de notas
areaTexto = tk.Text(ventana)
areaTexto.pack(fill=tk.BOTH, expand=True)

# Agregar comandos al menú de Archivo y Edición
archivo.add_command(label="Nuevo", command = nuevo_archivo)
archivo.add_command(label="Abrir", command=abrir_archivo) 
archivo.add_command(label="Guardar", command=guardar_archivo)
archivo.add_command(label="Guardar como", command=guardar_como)

# Agregar comandos al menú de Edición
edicion.add_command(label="Copiar", command=copiar)
edicion.add_command(label="Pegar", command=pegar)
edicion.add_command(label="Cortar", command=cortar)

# Agregar un separador al menú de Edición
ventana.mainloop()