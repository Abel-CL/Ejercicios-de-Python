"""
Crea un programa que tome una lista de números y genere una nueva lista que contenga solo los números pares de la lista original.
"""

# Lista original de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista para almacenar los números pares
num_par = []

# Iterar sobre cada número en la lista original
for numero in numeros:
    # Verificar si el número es par
    if numero % 2 == 0:
        # Agregar el número par a la nueva lista
        num_par.append(numero)

# Imprimir la lista de números pares
print(num_par)
