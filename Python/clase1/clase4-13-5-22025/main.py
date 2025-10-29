from leer_datos import carga_productos

def mostrar_productos(productos):
    print("Lista de productos:")
    for producto in productos:
        print(f" {producto['id']} : {producto['nombre']} - {producto['precio']}")

if __name__ == "__main__":
    ruta_archivo = 'productos.csv'
    productos = carga_productos(ruta_archivo)
    mostrar_productos(productos)