def suma(x, y):
    return x + y

print(suma(5, 3)) 


suma_lambda = lambda x, y: x + y

print(suma_lambda(5, 3))  

def crear_suma(n):
    return lambda x: x + n

suma_closure = crear_suma(3)
print(suma_closure(5))  

#----------------------------------------------------------------------------------------------------------
def collatz():
    return lambda n: [n := n // 2 if n % 2 == 0 else 3 * n + 1 for _ in range(100) if n != 1]

collatz_func = collatz()
print(collatz_func(6))  # Devuelve la secuencia de Collatz para 6