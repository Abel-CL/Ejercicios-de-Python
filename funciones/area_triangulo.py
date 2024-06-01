"""
Dada la base B y altura H de un triángulo rectángulo, hallar su área y desplegar sus lados y el área obtenida.
"""

# Definir una función para calcular el área de un triángulo rectángulo
def calcular(b, h):
    # Calcular el área del triángulo
    area = b * h / 2
    return area

# Definir una función para leer la base y altura del triángulo del usuario
def leerNumeros():
    # Leer la base del triángulo del usuario
    b = float(input("Ingrese la base del triángulo: "))
    # Leer la altura del triángulo del usuario
    h = float(input("Ingrese la altura del triángulo: "))
    return b, h

# Leer la base y altura del triángulo del usuario
base, altura = leerNumeros()

# Calcular el área del triángulo
area = calcular(base, altura)

# Desplegar el área del triángulo y sus lados
print(f"El área del triángulo es {area}, con una base de {base} unidades y una altura de {altura} unidades.")
