from generador_reportes import (
    cargar_datos,
    reporte_ventas_por_producto,
    promedio_salarios_por_departamento,
    datos_cliente
)
clientes = r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\CLASE3-12-05-2025\Hecho-en-clase\clientes.txt'
productos = r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\CLASE3-12-05-2025\Hecho-en-clase\productos.txt'
ventas_diarias = r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\CLASE3-12-05-2025\Hecho-en-clase\ventas_diariax.txt'
empleados = r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\CLASE3-12-05-2025\Hecho-en-clase\empleados.txt'
inventario = r'C:\Users\alejo\OneDrive\Documents\intecap\Python\clase1\CLASE3-12-05-2025\Hecho-en-clase\inventario.txt'



reporteUno = cargar_datos(ventas_diarias)
reporteDos = cargar_datos(empleados)
lista_clientes = cargar_datos(clientes)

reporte_ventas_por_producto(reporteUno)
promedio_salarios_por_departamento(reporteDos)
datos_cliente(lista_clientes)
