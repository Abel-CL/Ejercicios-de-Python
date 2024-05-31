"""
Escribe un programa que cuente el número de vocales en una cadena.
"""

# Cadena de entrada
cadena = "Hola, soy abel DB"

# Vocales
vocales = "aeiouAEIOU"

# Contador de vocales
contador = 0

# Contar el número de vocales en la cadena
for caracter in cadena:
    if caracter in vocales:
        contador += 1

# Imprimir el resultado
print(contador)
