"""
Crea una función recursiva que imprima un conteo regresivo desde un número dado hasta cero.
"""

# Definir una función recursiva para realizar un conteo regresivo
def conteo_regresivo(n):
    # Caso base: si n es menor que 0, imprimir "¡Despegue!"
    if n < 0:
        print("¡Despegue!")
    # Caso recursivo: imprimir el número actual y llamar a la función con n - 1
    else:
        print(n)
        conteo_regresivo(n - 1)

# Solicitar al usuario un número para iniciar el conteo regresivo
numero = int(input("Ingresa un número para el conteo regresivo: "))

# Iniciar el conteo regresivo
conteo_regresivo(numero)
