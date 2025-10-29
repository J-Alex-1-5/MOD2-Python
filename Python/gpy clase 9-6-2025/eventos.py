import tkinter as tk

import botones

ventana = tk.Tk()
ventana.title("Ejemplo eventos")
ventana.configure(bg="cyan")
ventana.geometry("400x300")

def evento_click(event):
    print("Botón presionado en la posición:")

    boton = tk.Button(ventana, text="Click aquí")
    boton.pack()

botones.bind("<Button-3>", evento_click)  # Asocia el evento de clic izquierdo del ratón

def on_key_press(event):
    if event.char == 'q':
        print("Tecla 'q' presionada, cerrando la ventana.")
        
        
ventana.bind("<KeyPress>", on_key_press)  # Asocia el evento de tecla presionada

ventana.mainloop()