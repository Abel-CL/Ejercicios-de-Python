"""
Crea un diccionario que contenga nombres de frutas y sus precios.
Luego, calcula el precio total si el usuario compra cierta cantidad de cada fruta.
"""

# Crear un diccionario con nombres de frutas y sus precios
precios = {"Manzana": 2.5, "Banana": 1.8, "Naranja": 3.0}

# Inicializar el total en 0
total = 0

# Solicitar al usuario ingresar la cantidad de cada fruta y calcular el precio total
for fruta, precio in precios.items():
    cantidad = int(input(f'Ingrese la cantidad de {fruta}: '))
    total += cantidad * precio  # Sumar el costo de las frutas al total

# Mostrar el precio total al usuario
print("El precio total es: ", total)
