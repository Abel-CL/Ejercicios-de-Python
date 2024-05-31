"""
Haz una calculadora básica pida al usuario dos valores, a y b.

Según la opción que desean, realizar la operación:

Si operación es 1 entonces debemos ver el resultado de a + b
Si operación es 2 entonces debemos ver el resultado de a * b
Si operación es 3 entonces debemos ver el resultado de a - b
Si operación es 4 entonces debemos ver el resultado de a / b
"""

# Se imprime un mensaje de bienvenida y se muestra el menú de opciones para elegir la operación.
print('\nCalculadora:\n1.- Suma\n2.- Multiplicacion\n3.- Resta\n4.- Division')

# Se solicita al usuario que ingrese la operación que desea realizar (del 1 al 4).
operacion = int(input('Ingrese la operacion que desea resolver (1 a 4): '))

# Se solicitan al usuario los valores para a y b.
a = int(input('\nIngrese un valor para A: '))
b = int(input('\nIngrese otro valor para B: '))

# Se utiliza una estructura condicional para determinar la operación a realizar.
if operacion == 1:
    # Si la operación es 1, se realiza la suma.
    resultado = a + b
    operacion_str = 'Suma'
elif operacion == 2:
    # Si la operación es 2, se realiza la multiplicación.
    resultado = a * b
    operacion_str = 'Multiplicación'
elif operacion == 3:
    # Si la operación es 3, se realiza la resta.
    resultado = a - b
    operacion_str = 'Resta'
elif operacion == 4:
    # Si la operación es 4, se realiza la división.
    if b != 0:
        resultado = a / b
        operacion_str = 'División'
    else:
        # Si el divisor es cero, se muestra un mensaje de error y se sale del programa.
        print("Error! No se puede dividir entre cero")
        exit()  # Salir del programa si hay un error de división por cero
else:
    # Si el usuario ingresa una opción inválida, se muestra un mensaje de error y se sale del programa.
    print("Error! La operación no existe")
    exit()  # Salir del programa si la operación no es válida

# Se muestra el resultado de la operación realizada, con formato de dos decimales.
print(f'\nLa {operacion_str} de {a} y {b} es: {resultado:.2f}')
