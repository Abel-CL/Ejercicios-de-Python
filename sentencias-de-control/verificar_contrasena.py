"""
Escribir un programa que almacene la cadena de caracteres contrsena en una variable,
pregunte al usuario por la contrasena e imprima por pantalla si la contrasena introducida por el usuario coincide
con la guardada en la variable sin tener en cuenta mayusculas y minusculas.
"""

# Se define la contraseña como una cadena de caracteres.
clave = "contrasena"

# Se solicita al usuario que ingrese la contraseña.
contrasena = input("Ingrese la contrasena: ")

# Se compara la contraseña ingresada por el usuario con la contraseña guardada, convirtiendo ambas a minúsculas.
# Esto se hace utilizando el método lower() para convertir ambas cadenas a minúsculas antes de compararlas.
if clave == contrasena.lower():
    # Si las contraseñas coinciden, se imprime un mensaje indicando que la contraseña coincide.
    print("La contrasena coincide")
else:
    # Si las contraseñas no coinciden, se imprime un mensaje indicando que la contraseña no coincide.
    print("La contrasena no coincide")
