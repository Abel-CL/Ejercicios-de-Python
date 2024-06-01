"""
Hacer leer G grados, M minutos y S segundos, convertir a radianes y desplegar el resultado.
"""

# Definir una función para calcular los radianes a partir de grados, minutos y segundos
def calcular(g, m, s):
    # Definir el valor de PI
    PI = 3.1416
    # Calcular el factor de conversión de grados a radianes
    factor_conversion = PI / 180
    # Calcular los radianes
    rad = factor_conversion * (g + m / 60 + s / 3600)
    return rad

# Definir una función para leer los grados, minutos y segundos del usuario
def leerGrado():
    # Solicitar al usuario que ingrese los grados, minutos y segundos
    g = int(input("Ingrese el grado: "))
    m = int(input("Ingrese los minutos: "))
    s = int(input("Ingrese los segundos: "))
    return g, m, s

# Leer los grados, minutos y segundos del usuario
grados, minutos, segundos = leerGrado()

# Calcular los radianes a partir de los grados, minutos y segundos ingresados
resultado = calcular(grados, minutos, segundos)

# Desplegar el resultado en radianes
print("El resultado en radianes es:", resultado)
