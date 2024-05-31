"""
Crea un diccionario que contenga nombres de personas y sus edades.
Luego, imprime solo los nombres de las personas que tienen más de 30 años.
"""

# Crear un diccionario con nombres de personas y sus edades
personas = {"Juan": 25, "María": 30, "Luisa": 28, "Pedro": 35, "Ana": 40}

# Iterar sobre cada par de nombre y edad en el diccionario
for nombre, edad in personas.items():
    # Verificar si la edad es mayor a 30
    if edad > 30:
        # Imprimir el nombre de la persona
        print(f"{nombre}")
