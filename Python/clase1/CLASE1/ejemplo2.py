# sistema de Gestion estudiantes
estudiantes = [] # lista de diccionarios

def registrar_estudiante():
    try:
        nombre = input("Ingresar el nombre del estudiante:")
        edad = int(input("ingresar la edad del estudiante:"))
        curso = input("Ingresar la carrera del estudiantre")
        notas = [] # Lista de notas
        while len(notas) < 3:
            nota = float(input("ingresar una nota"))
            notas.append(nota)
        estudiante = {"Nombre": nombre, "edad":edad, "Curso":curso, "Notas": notas}
        estudiante.append(estudiante) #agregar un estudiante a la lista
    except ValueError:
        print  ("Error: Datos invalidos")

def buscar_estudiante():
    nombre = input("Ingresar el nombre del estudiante a buscar: ") 
    encontrados = [estudiante for estudiante in estudiantes if estudiante["Nombre"].lower()==nombre.lower()]

    encontrados = []
    for estudiante in estudiantes:
        if estudiante["Nombre"].lower() == nombre.lower():
            encontrados.append(estudiante)

def mostrar_estadistica():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    todas_notas = [nota for estudiante in estudiantes for nota in estudiante["Notas"]]
    promedio_general = sum(todas_notas) / len(todas_notas)
    print("promedio general de notas: ", promedio_general)
    print("Maxima nota:", max(todas_notas))
    print("Minimo nota:", min(todas_notas))

while True:
    print("Siste")