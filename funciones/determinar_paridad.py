"""
Dado un número A, determinar si es par o impar mediante restas sucesivas, desplegar el número y el mensaje.
"""

# Definir una función para determinar si un número es par o impar mediante restas sucesivas
def calcular(a):
    b = a  # Guardar el valor original de 'a'
    while a >= 2:
        a -= 2  # Restar 2 de 'a' en cada iteración
    
    # Verificar si el número es par o impar
    if a == 0:
        print(f"El número {b} es par.")
    else:
        print(f"El número {b} es impar.")

# Definir una función para leer un número del usuario
def leerNumero():
    a = int(input("Ingrese un número: "))
    return a

# Leer el número del usuario
numero = leerNumero()

# Determinar si el número es par o impar
calcular(numero)
