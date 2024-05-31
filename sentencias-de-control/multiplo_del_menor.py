"""
Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
"""

# Se solicita al usuario que ingrese dos números enteros.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Se utiliza una estructura condicional para comparar los números ingresados.
if num1 > num2:
    # Si el primer número es mayor que el segundo, se verifica si el primero es múltiplo del segundo.
    if (num1 % num2) == 0:
        # Si el resto de la división del primer número entre el segundo es cero, entonces el primer número es múltiplo del segundo.
        print(f"{num1} es múltiplo de {num2}")
    else:
        # Si el resto de la división del primer número entre el segundo no es cero, entonces el primer número no es múltiplo del segundo.
        print(f"{num1} no es múltiplo de {num2}")
elif num2 > num1:
    # Si el segundo número es mayor que el primero, se verifica si el segundo es múltiplo del primero.
    if (num2 % num1) == 0:
        # Si el resto de la división del segundo número entre el primero es cero, entonces el segundo número es múltiplo del primero.
        print(f"{num2} es múltiplo de {num1}")
    else:
        # Si el resto de la división del segundo número entre el primero no es cero, entonces el segundo número no es múltiplo del primero.
        print(f"{num2} no es múltiplo de {num1}")
else:
    # Si los dos números son iguales, se muestra un mensaje indicando que son iguales y no se puede determinar si uno es múltiplo del otro.
    print("Los dos números son iguales")
