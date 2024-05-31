"""
Crea dos conjuntos y permite al usuario ingresar elementos para agregar a cada conjunto.
Luego, encuentra la unión de los conjuntos y muéstrala al usuario.
"""

# Crear dos conjuntos vacíos
set1 = set()
set2 = set()

# Solicitar al usuario ingresar elementos para el primer conjunto
while True:
    elemento1 = input("Ingrese un elemento para el primer conjunto (o 'fin' para terminar): ")
    if elemento1 == 'fin':
        break
    set1.add(elemento1)  # Agregar el elemento al primer conjunto

# Solicitar al usuario ingresar elementos para el segundo conjunto
while True:
    elemento2 = input("Ingrese un elemento para el segundo conjunto (o 'fin' para terminar): ")
    if elemento2 == 'fin':
        break
    set2.add(elemento2)  # Agregar el elemento al segundo conjunto

# Encontrar la unión de los dos conjuntos
union = set1.union(set2)

# Mostrar la unión de los conjuntos al usuario
print("Unión de los conjuntos:", union)
