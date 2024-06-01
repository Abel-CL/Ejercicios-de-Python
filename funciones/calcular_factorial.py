"""
Crea una función que calcule el factorial de un número ingresado por el usuario.
"""

# Solicitar al usuario ingresar un número
n = int(input("Ingrese un número: "))

# Definir la función factorial que calcula el factorial de un número de forma recursiva
def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Llamar a la función factorial y mostrar el resultado
print(factorial(n))
