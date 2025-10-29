#abtraccion: es el proceso de 
class Animal:
    def hablar(self):
        print("el animal hace un sonido")

class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

        def hablar(self):
            print(" guau guau")

animal = Animal()
perro = Perro("Firulais")
animal.hablar()  # Imprime "el animal hace un sonido"

class Gato:
    def hablar(self):
        return "miau miau"

class Gallo:
    def hablar(self):
        return "kikiriki"
    
class Pajaro:
    def hablar(self):
        return "pío pío"
    
def hacer_sonido(animal):
    print(animal.hablar())

hacer_sonido(Gato())  # Imprime " guau guau"
hacer_sonido(Gallo())  # Imprime "kikiriki"
hacer_sonido(Pajaro())  # Imprime "pío pío"

# abtraccion  -- interfas
from abc import ABC, abstractmethod


class figura(ABC):
    @abstractmethod
    def area(self):
        pass
class Cuadrado(figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
class Circulo(figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio
    
square = Cuadrado(5)
circle = Circulo(3)
print(f"El área del cuadrado es: {square.area()}")  # Imprime "El área del cuadrado es: 25" 
print(f"El área del círculo es: {circle.area()}")  # Imprime "El área del círculo es: 28.26"

# encapsulamiento
class Cueenta:
    def __init__(self,saldo):
        self._saldo = saldo

    def getSaldo(self):
        return self._saldo
    
    def setSaldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            print("el saldo se ha actualizado correctamente.")
        else:
            self._saldo = nuevo_saldo
            print(f"saldo actualizaado : Q {self._saldo}")	

cuenta = Cueenta(1000)
print(cuenta.getSaldo())  # Imprime 1000   
cuenta.setSaldo(1500)  # Imprime "el saldo se ha actualizado correctamente."

