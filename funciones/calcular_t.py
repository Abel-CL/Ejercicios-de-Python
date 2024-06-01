"""
Hacer leer dos numeros A y B, evaluar la expresion T = 2 + A + B, almacenar el resultado en T. Desplegar el resultado.
"""

# Definir una función para calcular T = 2 + A + B
def calcular_T(a, b):
    return 2 + a + b

# Definir una función para leer dos números del usuario
def leer_numeros():
    numeros = []
    # Solicitar al usuario que ingrese el valor de A
    numeros.append(int(input("Ingrese el valor de A: ")))
    # Solicitar al usuario que ingrese el valor de B
    numeros.append(int(input("Ingrese el valor de B: ")))
    return numeros

# Leer los números A y B del usuario
numeros = leer_numeros()

# Calcular el resultado de T usando los números ingresados
resultado = calcular_T(numeros[0], numeros[1])

# Desplegar el resultado de T
print(resultado)
