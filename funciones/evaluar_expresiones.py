"""
Hacer leer un numero A, evaluar sucesivamente las expresiones siguientes y desplegar los resultados obtenidos.
"""

# Definir una función para calcular las expresiones sucesivas basadas en el valor de A
def calcular(a):
    # Primera expresión: b = a + 10
    b = a + 10
    # Segunda expresión: c = 2 * b + a
    c = 2 * b + a
    # Tercera expresión: d = a + b + c + 5
    d = a + b + c + 5
    return d

# Definir una función para leer un número del usuario
def leerNumeros():
    # Solicitar al usuario que ingrese un número
    a = int(input("Ingrese un numero: "))
    return a

# Leer el número A del usuario
a = leerNumeros()

# Calcular el resultado de las expresiones usando el número ingresado
resultado = calcular(a)

# Desplegar el resultado de las expresiones
print(resultado)
