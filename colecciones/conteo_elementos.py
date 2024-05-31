"""
Escribe un programa que cuente la cantidad de veces que cada elemento
aparece en una lista usando un diccionario.
"""

# Lista de elementos
lista = ['a', 'b', 'a', 'c', 'b', 'a', 'd']

# Diccionario para contar la cantidad de veces que aparece cada elemento
diccionario = {}

# Contar la cantidad de veces que aparece cada elemento en la lista
for elemento in lista:
    if elemento in diccionario:
        diccionario[elemento] += 1
    else:
        diccionario[elemento] = 1

# Imprimir el diccionario con las cuentas
print(diccionario)
