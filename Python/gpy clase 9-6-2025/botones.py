import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")     
ventana.configure(bg="purple4")



boton = tk.Button(ventana, text="presiona")
boton.configure(bg="gray1", fg="white", font=("Arial", 14))
boton.pack()

def presionar_boton():
    boton.config(text="¡Botón presionado!")
    print("Botón presionado")

boton.config(command=presionar_boton)
ventana.mainloop()