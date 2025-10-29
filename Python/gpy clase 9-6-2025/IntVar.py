import tkinter as tk
ventana = tk.Tk()

entero = tk.IntVar(value=35)
print(entero.get())

enterocheck = tk.IntVar(value=35)
print(enterocheck.get())

radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=entero, value=1)
radio1.pack()

radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=entero, value=2)
radio2.pack()

casilla = tk.Checkbutton(ventana, text="aceptar", variable=enterocheck, onvalue=1, offvalue=0)
casilla.pack()


def actualizar(*args):
    print(entero.get())

entero.trace_add("write", actualizar)


def actuazarCheck(*args):
    print(enterocheck.get())

enterocheck.trace_add("write", actuazarCheck)



ventana.mainloop()