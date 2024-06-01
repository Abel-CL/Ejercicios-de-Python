"""
Hacer leer un número X, hallar su cuadrado, cubo, raíz cuadrada, raíz cúbica y desplegar resultados.
"""

# Definir una función para calcular el cuadrado, cubo, raíz cuadrada y raíz cúbica de un número
def calcular(x):
    # Calcular el cuadrado
    cua = x * x
    # Calcular el cubo
    cub = x * x * x
    # Calcular la raíz cuadrada
    r_cua = x ** (1/2)
    # Calcular la raíz cúbica
    r_cub = x ** (1/3)
    return cua, cub, r_cua, r_cub

# Definir una función para leer un número del usuario
def leerNumero():
    # Solicitar al usuario que ingrese un número
    x = int(input("Ingrese un número: "))
    return x

# Leer el número del usuario
numero = leerNumero()

# Calcular el cuadrado, cubo, raíz cuadrada y raíz cúbica del número ingresado
resultados = calcular(numero)

# Desplegar los resultados
print("Cuadrado:", resultados[0])
print("Cubo:", resultados[1])
print("Raíz cuadrada:", resultados[2])
print("Raíz cúbica:", resultados[3])
