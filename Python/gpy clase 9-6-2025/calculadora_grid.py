import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.configure(bg="purple1")


for i in range(4):
    ventana.columnconfigure(i, weight=1)
    ventana.rowconfigure(i+1, weight=1)


entry = tk.Entry(ventana, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")


botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for texto, fila, columna in botones:
    tk.Button(ventana, text=texto, font=("Arial", 20), width=5, height=2).grid(row=fila, column=columna, sticky="nsew")

ventana.mainloop()