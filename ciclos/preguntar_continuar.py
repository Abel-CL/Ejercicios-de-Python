"""
Escriba un programa que pregunte una y otra vez si desea continuar con el programa,
siempre que se conteste exactamente si (en minúsculas).
"""

# Preguntar al usuario si desea continuar
pregunta = input('¿Desea continuar? ')

# Mientras la respuesta sea 'si', continuar preguntando
while pregunta == 'si':
    pregunta = input('¿Desea continuar? ')

# Imprimir mensaje de fin del programa cuando la respuesta no sea 'si'
print('Fin del programa.')
