#Programacion orientada a objetos

#clase y objeto
class ejemmplo:
    def saludar(self):
        print("Hola, soy una persona")

pesona = ejemmplo()
pesona.saludar()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


## Ejemplo de uso de la clase Persona


class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

@classmethod
def desde_cadena(cls, cadena):
    nombre = cadena.split(",")[0] #divide la cadena por comas y toma el primer elemento
    apellido = cadena.split(",")[2] 
    return cls(nombre, apellido)

u1 = Usuario("Juan,21,Perez")
print(u1.nombre)  # Imprime "Juan"
print(u1.apellido)  # Imprime "Perez"
print(u1.edad)  # Imprime 21

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self_clave = "123"

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad} unidades. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        clave_vieja = input("Ingrese la clave de la cuenta: ")
        if clave_vieja != self._clave:
            print("Clave incorrecta. No se puede retirar dinero.")
            return
        else:
                self._clave = clave_vieja


            print("Clave correcta. Procediendo con el retiro.")
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} unidades. Nuevo saldo: {self.saldo}")