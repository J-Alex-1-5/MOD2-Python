import generador_reportes as gr

# Cargar los datos desde un archivo (debes reemplazar 'datos.txt' con el archivo correcto)
archivo = "datos.txt"
datos = gr.cargar_datos(archivo)

if datos is not None:
    print("** Reporte de Ventas por Producto **")
    print(gr.reporte_ventas_por_producto(datos))

    print("\n** Promedio de Salarios por Departamento **")
    print(gr.promedio_salarios_por_departamento(datos))

    print("\n** Productos con Bajo Inventario **")
    print(gr.productos_bajo_inventario(datos))

    print("\n** Listado de Clientes Registrados **")
    print(gr.listado_clientes_registrados(datos))