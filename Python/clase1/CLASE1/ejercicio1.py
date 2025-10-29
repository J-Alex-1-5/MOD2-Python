
inventario_equipo_deportes = []  

def agregar_producto():
    try:
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad disponible: "))
        precio = float(input("Ingrese el precio del producto: "))
        producto = {"Código": codigo, "Nombre": nombre, "Cantidad": cantidad, "Precio": precio}
        inventario_equipo_deportes.append(producto)  
    except ValueError:
        print("Error: Datos inválidos")

def modificar_cantidad():
    codigo = input("Ingrese el código del producto para modificar la cantidad: ")
    for producto in inventario_equipo_deportes:
        if producto["Código"] == codigo:
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                producto["Cantidad"] = nueva_cantidad
                print("Cantidad actualizada correctamente.")
                return
            except ValueError:
                print("Error: Ingrese un número válido.")
    print("Producto no encontrado.")

def mostrar_inventario():
    if not inventario_equipo_deportes:
        print("No hay productos registrados.")
        return
    for producto in inventario_equipo_deportes:
        print(f"Código: {producto['Código']}, Nombre: {producto['Nombre']}, Cantidad: {producto['Cantidad']}, Precio: {producto['Precio']}")

def mostrar_estadisticas():
    if not inventario_equipo_deportes:
        print("No hay productos registrados.")
        return
    precios = [producto["Precio"] for producto in inventario_equipo_deportes]
    promedio_precio = sum(precios) / len(precios)
    print(f"Precio promedio: {promedio_precio:.2f}")
    print(f"Precio máximo: {max(precios):.2f}")
    print(f"Precio mínimo: {min(precios):.2f}")