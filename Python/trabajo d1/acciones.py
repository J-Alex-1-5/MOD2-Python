from utilidades import leer_usuarios, escribir_usuario # error en sintaxis en leer_usuario

def ver_usuarios(ruta):
    usuarios = leer_usuarios(ruta)# error en sintaxis en leer_usuario
    if not usuarios :  # if usuarios == []: esta mal utilizado
        print("Archivo vacío") 
    else:
        for usuario in usuarios: #in usuarios:
            print(usuario)

def agregar_usuario(ruta):
    nombre = input("Nombre del nuevo usuario: ")
    if nombre == "": # nombre ="":
        print("No se puede agregar un usuario sin nombre")
        return
    escribir_usuario(ruta, nombre)  # (ruta nombre)
