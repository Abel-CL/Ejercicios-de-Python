"""
Calcular el factorial de un número N, mostrar el número y su factorial.
"""

# Definir una función para calcular el factorial de un número
def calcular(n):
    factorial = 1
    # Multiplicar los números del 1 al 'n' para calcular el factorial
    for c in range(1, n + 1):
        factorial = factorial * c
    return factorial

# Definir una función para leer un número del usuario
def leerNumero():
    n = int(input("Ingrese un número: "))
    return n

# Leer el número del usuario
numero = leerNumero()

# Calcular el factorial del número
resultado = calcular(numero)

# Mostrar el número y su factorial
print("El factorial de {} es {}".format(numero, resultado))
