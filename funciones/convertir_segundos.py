"""
Hacer leer S en segundos, convertir a minutos y horas, y desplegar resultados.
"""

# Definir una función para convertir segundos a horas
def calcular(s):
    # Calcular los minutos
    minutos = s // 60
    # Calcular las horas
    horas = minutos // 60
    return horas

# Definir una función para leer un número de segundos del usuario
def leerNumeros():
    # Solicitar al usuario que ingrese un número de segundos
    s = int(input("Ingrese un numero: "))
    return s

# Leer el número de segundos del usuario
seg = leerNumeros()

# Calcular las horas a partir de los segundos ingresados
resultado = calcular(seg)

# Desplegar el resultado en horas
print(resultado)
