import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo plays")
ventana.configure(bg="purple1")

boton1 = tk.Button(ventana, text="Botón 1")
boton1.place(relx=0.25, rely=0.10)

boton2 = tk.Button(ventana, text="Botón 2")
boton2.place(relx=0.25, rely=0.30)



ventana.mainloop()