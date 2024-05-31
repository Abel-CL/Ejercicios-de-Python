"""
Enunciado: Usa una tupla para almacenar los días de la semana y permite que el usuario ingrese un número del 1 al 7
para devolver el día correspondiente.
"""

# Definimos una tupla con los días de la semana
dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')

# Solicitamos al usuario que ingrese un número del 1 al 7
numero = int(input("Ingresa un número del 1 al 7: "))

# Verificamos que el número esté en el rango válido (1 a 7)
if 1 <= numero <= 7:
    # Si el número es válido, imprimimos el día correspondiente de la tupla
    print(f"El día correspondiente es: {dias[numero - 1]}")
else:
    # Si el número no es válido, imprimimos un mensaje de error
    print("Número inválido.")
