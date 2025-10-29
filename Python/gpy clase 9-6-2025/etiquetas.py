import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo de etiquetas") 
ventana.configure(bg="purple4")

etiqueta = tk.Label(ventana, text="Hola, mundo")
etiqueta.configure(bg="gray1", fg="white", font=("Arial", 14, "bold"))
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)

actualizar_hora()


ventana.mainloop()