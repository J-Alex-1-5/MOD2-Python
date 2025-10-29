# se importa la libreria tkinter para crear la GUI de la calculadora agreganfo botones y una pantalla
import tkinter as tk
ventana = tk.Tk()
valor_a = 0 
valor_b = 0
operacion = "Sumar"


#Funciones / se agragan operaciones para sumas, restar, dividir, multiplicar y borrar.
# esta funcion se utiliza para sumr los 2 valores introducidor por el usuario
def sumar():
    global valor_a
    global valor_b
    return valor_a + valor_b

# esta funcion se utiliza para restar los 2 valores introducidor por el usuario
def restar():
    global valor_a
    global valor_b
    return valor_a - valor_b

# esta funcion se utiliza para multiplicar los 2 valores introducidor por el usuario
def multiplicar():
    global valor_a
    global valor_b
    return valor_a * valor_b

# esta funcion se utiliza para dividir los 2 valores introducidor por el usuario
def dividir():
    try:
        global valor_a
        global valor_b
        return valor_a / valor_b
    except ZeroDivisionError:
        print("No se puede dividir entre 0...") # se agrgo un mensaje de error si el usuario intenta dividir entre 0

# esta funcion se utiliza para borrar la pantalla de la calculadora
def borrar():
    global pantalla
    pantalla.delete(0,tk.END)

# esta funcion se utiliza para agregar texto a la pantalla de la calculadora
def agregarTexto(valor):
    global pantalla
    pantalla.insert(tk.END, valor)

# esta funcion se utiliza para operar los valores introducidos por el usuario
def operar(simbolo):
    global pantalla
    global valor_a
    global operacion

# Se obtiene el valor introducido en la pantalla y se combierten par que se puede leer en el lenguaje de programacion
    valor_a = float(pantalla.get())
    pantalla.delete(0,tk.END)

# Se determina la operacion a realizar segun el simbolo introducido por el usuario, se utiliza un if-elif-else para determinar la operacion a realizar
    if simbolo == "/":
        operacion = "dividir"
    elif simbolo == "*":
        operacion = "multiplicar"
    elif simbolo == "-":
        operacion = "resta"
    else:
        operacion = "sumar"
    
    print(valor_a)
    print(operacion)

# esta funcion se utiliza para obtener el resultado de la operacion realizada
def res_igual():
    global pantalla
    global valor_a
    global valor_b
    global resultado
    global operacion

    valor_b = float(pantalla.get())
    pantalla.delete(0,tk.END)
    print(valor_b)

    evaluacion = eval(operacion)
    resultado = evaluacion()
    pantalla.insert(tk.END, resultado)
    print(resultado)


#GUI

#Pantalla
pantalla = tk.Entry(ventana, width=24, border=6,justify="right")
pantalla.grid(row=0,column=0, columnspan=4)


#Botones estos son los botones de la interfas grafica de la calculadora/ se utilizan para poder intereactuar con la calculadora
siete = tk.Button(ventana, text="7", width=4, command=lambda: agregarTexto(7))
siete.grid(row=1,column=0)

# los botones se trabajaron por separado para que cada uno tenga su propia funcion y se pueda agregar el texto correspondiente a la pantalla
ocho = tk.Button(ventana, text="8", width=4, command=lambda: agregarTexto(8))
ocho.grid(row=1,column=1)

nueve = tk.Button(ventana, text="9", width=4, command=lambda: agregarTexto(9))
nueve.grid(row=1,column=2)

division = tk.Button(ventana, text="/", width=4,command=lambda: operar("/"))
division.grid(row=1,column=3)

cuatro = tk.Button(ventana, text="4", width=4, command=lambda: agregarTexto(4))
cuatro.grid(row=2,column=0)

cinco = tk.Button(ventana, text="5", width=4, command=lambda: agregarTexto(5))
cinco.grid(row=2,column=1)

seis = tk.Button(ventana, text="6", width=4, command=lambda: agregarTexto(6))
seis.grid(row=2,column=2)

multiplicacion = tk.Button(ventana, text="*", width=4,command=lambda: operar("*"))
multiplicacion.grid(row=2,column=3)

tres = tk.Button(ventana, text="3", width=4, command=lambda: agregarTexto(3))
tres.grid(row=3,column=0)

dos = tk.Button(ventana, text="2", width=4, command=lambda: agregarTexto(2))
dos.grid(row=3,column=1)

uno = tk.Button(ventana, text="1", width=4, command=lambda: agregarTexto(1))
uno.grid(row=3,column=2)

resta = tk.Button(ventana, text="-", width=4,command=lambda:operar("-"))
resta.grid(row=3,column=3)

punto = tk.Button(ventana, text=".", width=4, command=lambda: agregarTexto("0"))
punto.grid(row=4,column=0)

cero = tk.Button(ventana, text="0", width=4, command=lambda: agregarTexto(0))
cero.grid(row=4,column=1)

igual = tk.Button(ventana, text="=", width=4,command=res_igual)
igual.grid(row=4,column=2)

suma = tk.Button(ventana, text="+", width=4,command=lambda:operar("+"))
suma.grid(row=4,column=3)

borrar = tk.Button(ventana, text="Borrar", width=20, command=borrar)
borrar.grid(row=5,column=0, columnspan=4)

# se inicia el bucle principal de la ventana para que se muestre la calculadora
ventana.mainloop()