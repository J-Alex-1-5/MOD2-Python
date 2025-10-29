def carga_productos(ruta_archivo):
    productos   = []
    try:
        whith open(ruta_archivo, 'r', encoding= 'utf-8') as archivo:
            encabeza = archivo.readline().strip().split(',')
        for linea in archivo:
            try:
                valores = linea.strip().split(',')
                if len(valores) != len(encabeza):
                    raise ValueError(f"Error en la línea: {linea.strip()}")
                
                producto = {encabeza[i]: valores[i] for i in range(len(encabeza))}
                producto['precio'] = float(producto['precio'])
                productos.append(producto)

                except ValueError as ex:
                    print(f'Error al procesar la línea: {linea.strip()} - {ex}')
    except FileNotFoundError:
        print   (f"El archivo {ruta_archivo} no existe.")

    return productos