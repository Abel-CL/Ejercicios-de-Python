"""
Escribe un programa que pida al usuario introducir números
uno por uno y calcule la suma de estos números.
El programa debe detenerse y dejar de pedir números
cuando el usuario introduzca un número negativo.
Finalmente, debe imprimir la suma de todos los números introducidos
antes del número negativo.
"""

# Inicializar la variable para almacenar la suma
suma = 0

# Bucle para solicitar números al usuario y calcular la suma
while True:
    numero = int(input("Introduce un número: "))
    if numero < 0:
        break
    suma += numero

# Imprimir la suma de todos los números ingresados antes del número negativo
print("La suma de todos los números hasta el primer número negativo es:", suma)
