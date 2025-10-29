import tkinter as tk
ventana = tk.Tk()

texto = tk.StringVar(value="Hola, mundo!")

entrada = tk.Entry(ventana, textvariable=texto)
entrada.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

def actualizar_etiqueta(*args):
    etiqueta.config(text=texto.get())

texto.trace_add("write", actualizar_etiqueta)

ventana.mainloop()