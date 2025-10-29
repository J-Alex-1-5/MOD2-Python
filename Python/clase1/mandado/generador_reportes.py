def cargar_datos(ruta_archivo):
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