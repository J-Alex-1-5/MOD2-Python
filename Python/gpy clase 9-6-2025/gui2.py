import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana") 
ventana.geometry("400x300")
ventana.minsize(400, 200)      
ventana.maxsize(800, 600)
ventana.configure(bg="purple4")



ventana.mainloop()  