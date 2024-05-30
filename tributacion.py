"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener
unos ingresos iguales o superiores a 1000 bs mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
y muestre por pantalla si el usuario tiene que tributar o no
"""

# Se solicita al usuario que ingrese su edad y sus ingresos mensuales.
edad = input('Ingrese su edad: ')
ingresos = input('Ingrese los ingresos mensuales: ')

# Se convierten la edad y los ingresos ingresados por el usuario a enteros y flotantes, respectivamente.
edad = int(edad)
ingresos = float(ingresos)

# Se verifica si el usuario cumple con los requisitos para tributar.
if edad > 16 and ingresos >= 1000:
    # Si la edad es mayor que 16 y los ingresos son iguales o superiores a 1000 bs, se imprime un mensaje indicando que el usuario tiene derecho a tributar.
    print('El usuario tiene derecho a tributar')
else:
    # Si no cumple con los requisitos, se imprime un mensaje indicando que el usuario no tiene derecho a tributar.
    print('El usuario no tiene derecho a tributar')
