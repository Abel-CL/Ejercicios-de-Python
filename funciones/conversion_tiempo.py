"""
Hacer leer S en segundos, convertir a minutos y horas, y desplegar resultados.
"""

# Definir una función para calcular horas, minutos y segundos
def calcular(s):
    # Calcular las horas
    horas = s // 3600
    # Calcular los minutos
    minutos = (s % 3600) // 60
    # Calcular los segundos restantes
    segundos_restantes = s % 60
    return horas, minutos, segundos_restantes

# Definir una función para leer el número de segundos del usuario
def leerNumeros():
    # Solicitar al usuario que ingrese un número de segundos
    s = int(input("Ingrese un número en segundos: "))
    return s

# Leer el número de segundos del usuario
segundos = leerNumeros()

# Calcular horas, minutos y segundos a partir de los segundos ingresados
horas, minutos, segundos_restantes = calcular(segundos)

# Desplegar el resultado en horas, minutos y segundos
print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos_restantes}")
