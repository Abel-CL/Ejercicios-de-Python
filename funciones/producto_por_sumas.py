"""
Dado dos números A y B, realizar el producto de los dos números por sumas sucesivas, almacenar el resultado en una variable P, mostrar el resultado.
"""

# Definir una función para calcular el producto de dos números mediante sumas sucesivas
def calcular(a, b):
    p = 0
    # Sumar 'a' a 'p', 'b' veces
    for _ in range(b):
        p = p + a
    return p

# Definir una función para leer dos números del usuario
def leerNumeros():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    return a, b

# Leer los dos números del usuario
num1, num2 = leerNumeros()

# Calcular el producto de los dos números
resultado = calcular(num1, num2)

# Mostrar el resultado del producto
print("El resultado es: ", resultado)
