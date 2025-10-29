def cargar_datos(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(',')
        datos = []
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            fila = {encabezados[i]: valores[i] for i in range(len(encabezados))}
            datos.append(fila)
        return datos


def reporte_ventas_por_producto(ventas):
    reporte = {}
    for venta in ventas:
        fecha = venta['fecha']
        producto = venta['producto']
        cantidad = int(venta['cantidad'])
        precio_unitario = float(venta['precio_unitario'])
        total = cantidad * precio_unitario

        if producto not in reporte:
            reporte[producto] = {'cantidad': 0, 'total': 0.0}
        
        reporte[producto]['cantidad'] += cantidad
        reporte[producto]['total'] += total
    
    print('REPORTE DE VENTAS POR PRODUCTO')
    for producto,datos in reporte.items():
        print(f"{producto}: {datos['cantidad']} unidades vendidas. Total: Q{datos['total']:.2f}")
    print('-----------------------------------')

def promedio_salarios_por_departamento(empleados):
    departamentos = {}

    for empleado in empleados:
        depto = empleado['departamento']
        salario = float(empleado['salario'])

        if depto not in departamentos:
            departamentos[depto] = []
        
        departamentos[depto].append(salario)

    print("PROMEDIO DE SALARIOS POR DEPARTAMENTO")
    for depto, salarios in departamentos.items():
        promedio = sum(salarios) / len(salarios)
        print(f"{depto}: Q{promedio:.2f}")
    print('-----------------------------------')

def productos_bajo_inventario(inventario,limite=20):
    pass


def datos_cliente(clientes):
    print("DATOS DE CLIENTES")
    for clientes in clientes:
        print(f"{clientes}")   
    print('-----------------------------------')