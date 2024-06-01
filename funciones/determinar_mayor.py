"""
Dado tres números A, B, C determinar y desplegar cual es mayor.
"""

# Definir una función para calcular cuál de los tres números es el mayor
def calcular(a, b, c):
    if a > b:  # Comparar 'a' con 'b'
        if a > c:  # Comparar 'a' con 'c'
            return a  # 'a' es el mayor
        else:
            return c  # 'c' es el mayor
    else:
        if b > c:  # Comparar 'b' con 'c'
            return b  # 'b' es el mayor
        else:
            return c  # 'c' es el mayor

# Definir una función para leer tres números del usuario
def leerNumero():
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    c = int(input("Ingrese el valor de c: "))
    return a, b, c

# Leer los tres números del usuario
n1, n2, n3 = leerNumero()

# Calcular y mostrar cuál es el número mayor
print("El número mayor es:", calcular(n1, n2, n3))
