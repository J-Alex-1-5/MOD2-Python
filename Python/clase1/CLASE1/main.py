from utils import funciones as f# type: ignore

while True:
    print("\n==========================")
    print("Sistema de Gestion de Estudiantes")
    print("1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Mostrar estadisticas")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        f.registrar_estudiante()
    elif opcion == "2":
        f.buscar_estudiante()
    elif opcion == "3":
        f.mostrar_estadisticas()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida, intente nuevamente.")