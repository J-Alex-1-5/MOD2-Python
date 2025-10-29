#tkinder es una libreria de Python que permite crear interfaces gráficas de usuario (GUI).


import tkinter as tk
ventana = tk.Tk()  
ventana.title("Mi primera ventana") 
ventana.geometry("400x300") 
ventana.minsize(400, 200)
ventana.maxsize(800, 600)

ventana.resizable(False, False)

ventana.configure(bg="purple4")

frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bg="gray1", bd=5)
frame1.pack()


frame2 = tk.Frame(frame1)
frame2.configure(width=100, height=100, bg="purple3", bd=5)
frame2.pack()


boton = tk.Button(frame1,text="hola.......")
boton.pack()


ventana.mainloop() 
