import tkinter as tk
ventana = tk.Tk()
ventana.title("Ejemplo con Frames")
ventana.configure(bg="cyan")

ventana.geometry("600x400")
ventana.minsize(400,200)
ventana.maxsize(800,600)


frame1 = tk.Frame(ventana) #Se crea un Frame y se le indica en donde se debe crear.
frame1.configure(width=300, height=200, bg="red", bd=5)
frame1.pack()

frame2 = tk.Frame(frame1)
frame2.configure(width=100,height=100, bg="blue",bd=5)
frame2.pack()
boton = tk.Button(frame1,text="Hola...")
boton.pack()

ventana.mainloop()