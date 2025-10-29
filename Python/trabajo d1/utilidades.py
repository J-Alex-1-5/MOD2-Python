

def leer_usuarios(archivo): # (archivo): error en sintaxis de :
    try: # try
        with open(archivo, '+r') as f: # error en declaracion debe ser 'r'
            lineas = f.readlines()
            usuarios = [linea.strip() for linea in lineas if linea != '']
            return usuarios
    except FileNotFoundError: # fieNotFoundErro
        print("Archivo no existe")
        return [] # corchetes

def escribir_usuario(archivo, nombre): # (archivo nombre)
    with open(archivo, 'a') as f :  # error en sintaxis de :
        f.write(nombre + '\n')

def mostrar_menu():
    print("Menu de usuarios")
    print("1. Ver usuarios")
    print("2. Agregar usuario")
    print("3. Salida")
    print("4. eliminar usuario") 


def eliminar_usuario(archivo):
    usuarios = leer_usuarios(archivo)
    if not usuarios:
        print("No hay usuarios para eliminar.")
        return
    
    for i, usuario in enumerate(usuarios):
        print(f"{i + 1}. {usuario}")

    try:
        indice = int(input("Número del usuario a eliminar: ")) - 1
        if 0 <= indice < len(usuarios):
            usuario_eliminado = usuarios.pop(indice)  # Remueve el usuario de la lista
            
            with open(archivo, 'w') as f:
                for usuario in usuarios:
                    f.write(usuario + '\n')
            
            print(f"Usuario '{usuario_eliminado}' eliminado correctamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Introduce un número.")
