"""
Leer números enteros de teclado,
hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números ingresados.
"""

# Solicitar al usuario que ingrese un número
num = int(input('Ingrese un numero: '))
# Inicializar la variable suma en 0
suma = 0

# Mientras el número ingresado no sea 0
while num != 0:
    # Sumar el número ingresado a la variable suma
    suma += num
    # Solicitar al usuario que ingrese otro número
    num = int(input("Ingrese otro numero (0 para finalizar): "))

# Mostrar la sumatoria de todos los números ingresados
print("La sumatoria de todos los numeros es: ", suma)
