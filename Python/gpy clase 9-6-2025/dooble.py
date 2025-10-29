import tkinter as tk
ventana = tk.Tk()

decimal = tk.DoubleVar(value=3.14)

control = tk.Scale(ventana, variable=decimal, from_=0, to=10, resolution=0.07, orient=tk.VERTICAL)
control.pack()


ventana.mainloop()