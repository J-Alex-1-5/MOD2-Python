import math
area = 5
radio = math.sqrt(area / math.pi)
print(f"El radio de un círculo con área {area} es: {radio:.4f}")







nombres = ["Alejandro", "Luis", "Maria", "Fernanda", "Jose", "Gabriela"]
for nombre in nombres:
    if len(nombre) > 5:
        print(nombre)


        frutas = {
            "manzana": 0.8,
            "pera": 1.2,
            "plátano": 0.9,
            "kiwi": 1.5,
            "naranja": 1.1
        }

        for fruta, precio in frutas.items():
            if precio > 1:
                print(f"{fruta}: {precio}")




                suma = sum(range(1, 101))
                print(f"La suma de los números del 1 al 100 es: {suma}")


                def es_primo(numero):
                    if numero < 2:
                        return False
                    for i in range(2, int(numero ** 0.5) + 1):
                        if numero % i == 0:
                            return False
                    return True

                # Ejemplo de uso
                num = 17
                if es_primo(num):
                    print(f"{num} es un número primo.")
                else:
                    print(f"{num} no es un número primo.")



#sjdklajskldjaskjdklasjdl



cadena = "  Hola Mundo Python  "
cadena_procesada = cadena.lower().replace(" ", "")
print(cadena_procesada)

#def 
try:
    texto = input("Introduce un número entero: ")
    numero = int(texto)
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: No se pudo convertir el texto a un número entero.")


#

colores = ("rojo", "verde", "azul")
for color in colores:
    print(color)

#
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 1, 6]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista sin duplicados: {lista_sin_duplicados}")

#Escribe un script que reciba una lista de números y cree una nueva lista solo con los números pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [n for n in numeros if n % 2 == 0]
print(f"Números pares: {numeros_pares}")
