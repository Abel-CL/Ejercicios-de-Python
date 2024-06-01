"""
Calcular el factorial de un número N, mostrar el número y su factorial mediante el proceso repetitivo while.
"""

# Definir una función para calcular el factorial de un número usando un bucle while
def calcular(n):
    factorial = 1
    c = 1
    # Usar un bucle while para calcular el factorial
    while c <= n:
        factorial = factorial * c
        c = c + 1
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
print("El factorial de", numero, "es", resultado)
