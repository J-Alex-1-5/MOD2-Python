import tkinter as tk
ventana = tk.Tk()

boleana = tk.BooleanVar(value=True)

casilla = tk.Checkbutton(ventana, text="aceptar", variable=boleana)
casilla.pack()


def actualizar(*args):
    print(boleana.get())

boleana.trace_add("write", actualizar)

ventana.mainloop()