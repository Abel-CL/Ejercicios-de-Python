"""
Leer dos números A y B, del mayor restarle el menor y desplegar el resultado.
"""

# Definir una función para calcular la diferencia entre el número mayor y el número menor
def calcular(a, b):
    # Comprobar cuál es el número mayor y restarle el menor
    if a > b:
        diferencia = a - b
    else:
        diferencia = b - a
    return diferencia
    
# Definir una función para leer dos números del usuario
def leerNumeros():
    # Leer el primer número del usuario
    a = int(input("Ingrese el primer número: "))
    # Leer el segundo número del usuario
    b = int(input("Ingrese el segundo número: "))
    return a, b

# Leer dos números del usuario
num1, num2 = leerNumeros()

# Calcular la diferencia entre el número mayor y el número menor
resultado = calcular(num1, num2)

# Desplegar el resultado de la resta
print("El resultado es:", resultado)
