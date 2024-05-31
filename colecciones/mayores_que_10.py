"""
Escribe un programa que tome una lista de números y luego imprima
"Sí" si todos los números en la lista son mayores que 10, de lo contrario, imprime "No".
"""

# Lista de números
numeros = [15, 20, 12, 25, 11]

# Iterar sobre la lista de números
for numero in numeros:
    if numero <= 10:  # Verificar si algún número es menor o igual que 10
        print('No')   # Imprimir 'No' si se encuentra un número menor o igual a 10
        break         # Salir del bucle
else:
    print('Si')       # Imprimir 'Si' si todos los números son mayores que 10
