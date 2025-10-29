import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(bg="purple1")


entry = tk.Entry(ventana, font=("Arial", 20), justify="right")
entry.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)


boton_7 = tk.Button(ventana, text="7", font=("Arial", 20) )
boton_7.place(relx=0.1, rely=0.2)

boton_8 = tk.Button(ventana, text="8", font=("Arial", 20))
boton_8.place(relx=0.35, rely=0.2)

boton_9 = tk.Button(ventana, text="9", font=("Arial", 20))
boton_9.place(relx=0.6, rely=0.2)

boton_div = tk.Button(ventana, text="/", font=("Arial", 20))
boton_div.place(relx=0.85, rely=0.2)

boton_4 = tk.Button(ventana, text="4", font=("Arial", 20))
boton_4.place(relx=0.1, rely=0.35)

boton_5 = tk.Button(ventana, text="5", font=("Arial", 20))
boton_5.place(relx=0.35, rely=0.35)

boton_6 = tk.Button(ventana, text="6", font=("Arial", 20))
boton_6.place(relx=0.6, rely=0.35)

boton_mult = tk.Button(ventana, text="*", font=("Arial", 20))
boton_mult.place(relx=0.85, rely=0.35)

boton_1 = tk.Button(ventana, text="1", font=("Arial", 20))
boton_1.place(relx=0.1, rely=0.5)

boton_2 = tk.Button(ventana, text="2", font=("Arial", 20))
boton_2.place(relx=0.35, rely=0.5)

boton_3 = tk.Button(ventana, text="3", font=("Arial", 20))
boton_3.place(relx=0.6, rely=0.5)

boton_resta = tk.Button(ventana, text="-", font=("Arial", 20))
boton_resta.place(relx=0.85, rely=0.5)

boton_0 = tk.Button(ventana, text="0", font=("Arial", 20))
boton_0.place(relx=0.1, rely=0.65)

boton_punto = tk.Button(ventana, text=".", font=("Arial", 20))
boton_punto.place(relx=0.35, rely=0.65)

boton_igual = tk.Button(ventana, text="=", font=("Arial", 20))
boton_igual.place(relx=0.6, rely=0.65)

boton_suma = tk.Button(ventana, text="+", font=("Arial", 20))
boton_suma.place(relx=0.85, rely=0.65)

ventana.mainloop()