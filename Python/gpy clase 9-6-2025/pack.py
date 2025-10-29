import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo eventos")   
ventana.configure(bg="cyan")

boton1 = tk.Button(ventana, text="Botón 1")
boton1.pack(side="right", padx=10, pady=10)