#Sistema de Gestion de Estudiantes
estudiantes = [] #Lista de diccionarios

def registrar_estudiante():
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        curso = input("Ingrese la carrera del estudiante: ")
        notas = [] #Lista de notas
        while len(notas) < 3:
            nota = float(input("Ingrese una nota: "))
            notas.append(nota)
        estudiante = {"Nombre":nombre, "Edad":edad, "Curso":curso, "Notas":notas}
        estudiantes.append(estudiante) #Agregar estudiante a la lista
    except ValueError:
        print("Error: Datos invalidos")

def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    encontrados = [estudiante for estudiante in estudiantes if estudiante["Nombre"].lower() == nombre.lower()] 

    if encontrados:
        for estudiante in encontrados:
            print("Nombre:", estudiante["Nombre"])
            print("Edad:", estudiante["Edad"])
            print("Curso:", estudiante["Curso"])
            print("Notas:", estudiante["Notas"])

def mostrar_estadisticas():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    todas_notas = [nota for estudiante in estudiantes for nota in estudiante["Notas"]]
    promedio_general = sum(todas_notas) / len(todas_notas)
    print("Promedio general de notas:", promedio_general)
    print("Maxima nota:", max(todas_notas))
    print("Minima nota:", min(todas_notas))

while True:
    print("\n==========================")
    print("Sistema de Gestion de Estudiantes")
    print("1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Mostrar estadisticas")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        buscar_estudiante()
    elif opcion == "3":
        mostrar_estadisticas()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida, intente nuevamente.")