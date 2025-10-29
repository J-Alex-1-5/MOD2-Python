def cargar_datos(ruta_archivo):
    print("** Reporte de clientes Registrados **")
    with open(ruta_archivo, 'r+', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(';')
        clientes = []
        for linea in lineas[1:]:
            valores = linea.strip().split(';')
            fila = {encabezados[i]: valores[i] for i in range(len(encabezados))}
            clientes.append(fila)
        return clientes

informacion = cargar_datos(r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\mandado\clientes.txt')



for fila in informacion:
    print(fila)


def cargar_datos(ruta_archivo):
    print("                        ")
    print("** Reporte de empleados Registrados **")
    with open(ruta_archivo, 'r+', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(',')
        empleados = []
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            fila = {encabezados[i]: valores[i] for i in range(len(encabezados))}
            empleados.append(fila)
        return empleados

informacion = cargar_datos(r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\mandado\empleados.txt')

for fila in informacion:
    print(fila)

def cargar_datos(ruta_archivo):
    print("                        ")
    print("** Reporte de inventario Registrado **")
    with open(ruta_archivo, 'r+', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(',')
        inventario = []
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            fila = {encabezados[i]: valores[i] for i in range(len(encabezados))}
            inventario.append(fila)
        return inventario

informacion = cargar_datos(r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\mandado\inventario.txt')

for fila in informacion:
    print(fila)

def cargar_datos(ruta_archivo):
    print("                        ")
    print("** Reporte de productos Registrados **")
    with open(ruta_archivo, 'r+', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(',')
        productos = []
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            fila = {encabezados[i]: valores[i] for i in range(len(encabezados))}
            productos.append(fila)
        return productos

informacion = cargar_datos(r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\mandado\productos.txt')

for fila in informacion:
    print(fila)

def cargar_datos(ruta_archivo):
    print("                        ")
    print("** Reporte de ventas_diarias Registradas **")
    with open(ruta_archivo, 'r+', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(',')
        ventas_diariax = []
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            fila = {encabezados[i]: valores[i] for i in range(len(encabezados))}
            ventas_diariax.append(fila)
        return ventas_diariax

informacion = cargar_datos(r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\mandado\ventas_diariax.txt')

for fila in informacion:
    print(fila)

    