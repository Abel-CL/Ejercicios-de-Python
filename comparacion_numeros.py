"""
Escriba un programa que pida tres números y que escriba si son:
Tres iguales
Dos igualeS
Tres distintos.
"""

# Se solicita al usuario que ingrese tres números.
num1 = int(input('Digite el primer número: '))
num2 = int(input('Digite el segundo número: '))
num3 = int(input('Digite el tercer número: '))

# Se utiliza una estructura condicional para determinar si los números son iguales o distintos.
if num1 == num2 and num1 == num3:
    # Si los tres números son iguales, se muestra un mensaje indicando que son tres iguales.
    print('Los números son Tres Iguales')
elif num1 == num2 != num3 or num1 == num3 != num2 or num2 == num3 != num1:
    # Si hay dos números iguales y uno diferente, se muestra un mensaje indicando que son dos iguales.
    print('Los números son Dos Iguales')
else:
    # Si los tres números son diferentes, se muestra un mensaje indicando que son distintos.
    print('Los números son Distintos')
