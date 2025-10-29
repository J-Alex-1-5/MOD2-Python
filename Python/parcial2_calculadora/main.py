import tkinter as tk
from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from dividir import dividir
from potencia import potencia

valor_a = 0
valor_b = 0
operacion = None

def borrar():
    pantalla.delete(0, tk.END)

def agregar_texto(valor):
    pantalla.insert(tk.END, valor)

def operar(simbolo):
    global valor_a, operacion

    valor_a = float(pantalla.get())
    pantalla.delete(0, tk.END)

    # Mapeo de operaciones, se optimizo la funcion de operar para poder usar un diccionario
    # y evitar el uso de if-elif-else
    operaciones = {"+": sumar, "-": restar, "*": multiplicar, "/": dividir, "!": potencia}
    operacion = operaciones.get(simbolo)

def res_igual():
    global valor_b, operacion

    valor_b = float(pantalla.get())
    pantalla.delete(0, tk.END)

    if operacion:
        resultado = operacion(valor_a, valor_b)
        pantalla.insert(tk.END, resultado)

# pantalla
ventana = tk.Tk()
pantalla = tk.Entry(ventana, width=24, border=6, justify="right")
pantalla.grid(row=0, column=0, columnspan=4)


# Botones
tk.Button(ventana, text="7", width=4, command=lambda: agregar_texto(7)).grid(row=1, column=0)
tk.Button(ventana, text="8", width=4, command=lambda: agregar_texto(8)).grid(row=1, column=1)
tk.Button(ventana, text="9", width=4, command=lambda: agregar_texto(9)).grid(row=1, column=2)
tk.Button(ventana, text="/", width=4, command=lambda: operar("/")).grid(row=1, column=3)

tk.Button(ventana, text="4", width=4, command=lambda: agregar_texto(4)).grid(row=2, column=0)
tk.Button(ventana, text="5", width=4, command=lambda: agregar_texto(5)).grid(row=2, column=1)
tk.Button(ventana, text="6", width=4, command=lambda: agregar_texto(6)).grid(row=2, column=2)
tk.Button(ventana, text="*", width=4, command=lambda: operar("*")).grid(row=2, column=3)

tk.Button(ventana, text="1", width=4, command=lambda: agregar_texto(1)).grid(row=3, column=0)
tk.Button(ventana, text="2", width=4, command=lambda: agregar_texto(2)).grid(row=3, column=1)
tk.Button(ventana, text="3", width=4, command=lambda: agregar_texto(3)).grid(row=3, column=2)
tk.Button(ventana, text="-", width=4, command=lambda: operar("-")).grid(row=3, column=3)

tk.Button(ventana, text="!", width=4, command=lambda: operar("!")).grid(row=4, column=0)
tk.Button(ventana, text="0", width=4, command=lambda: agregar_texto(0)).grid(row=4, column=1)
tk.Button(ventana, text="=", width=4, command=res_igual).grid(row=4, column=2)
tk.Button(ventana, text="+", width=4, command=lambda: operar("+")).grid(row=4, column=3)
tk.Button(ventana, text="Borrar", width=20, command=borrar).grid(row=5, column=0, columnspan=4)

ventana.mainloop()