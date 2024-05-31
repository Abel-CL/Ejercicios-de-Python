"""
Enunciado: Escribe un programa que calcule el promedio de una lista de calificaciones ingresadas por el usuario.
"""

# Lista para almacenar las calificaciones ingresadas por el usuario
calificaciones = []

# Bucle para solicitar calificaciones al usuario
while True:
    calificacion = input("Ingresa una calificación (o 'fin' para terminar): ")
    if calificacion.lower() == "fin":
        break
    calificaciones.append(float(calificacion))

# Calcular el promedio de las calificaciones
promedio = sum(calificaciones) / len(calificaciones)

# Imprimir el promedio
print(f"El promedio es: {promedio}")
