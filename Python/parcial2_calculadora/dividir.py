def dividir(valor_a, valor_b):
    try:
        return valor_a / valor_b
    except ZeroDivisionError:
        print("No se puede dividir entre 0...")
        return None