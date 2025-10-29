from utilidades import mostrar_menu, eliminar_usuario # error en sintaxis de menu utilizo tilde
from acciones import ver_usuarios, agregar_usuario # error en sintaxis de ver_usuario y agregar_usuarios

print("Inicio del programa...")

def main():
    archivo = "usuario.txt" #tx error en sintaxis
    while True:
        print("Ejecutando el menú...")
        mostrar_menu()
        opcion = input("Opcion:")

        if opcion == "1": # falta de comillas 
            ver_usuarios(archivo)
        elif opcion == '2': # dos error parametro o sintaxis
            agregar_usuario(archivo)
        
        elif opcion == "4": 
            eliminar_usuario(archivo)
        elif opcion == "3": # falta de comillas 


            break
if __name__ == "__main__":   # error en estructura debe agregarse __name__
    main()


