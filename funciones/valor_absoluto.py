"""
Hacer leer un número X, hallar su valor absoluto. Desplegar el resultado.
"""

# Definir una función para calcular el valor absoluto de un número
def calcular(x):
    # Si el número es negativo, multiplicarlo por -1 para hacerlo positivo
    if x < 0:
        x = x * (-1)
    # Devolver el valor absoluto
    return x
    
# Definir una función para leer un número del usuario
def leerNumero():
    # Leer un número del usuario
    x = float(input("Ingrese un número: "))
    return x

# Leer el número del usuario
num = leerNumero()

# Calcular el valor absoluto del número
resultado = calcular(num)

# Desplegar el resultado del valor absoluto
print("El valor absoluto de", num, "es", resultado)
