"""
Escribe un programa que pida al usuario dos numeros y devuelva su division,
si el usuario no introduce ningun numero debe devolver un aviso de error y si el divisor es cero tambien.
"""

# Se solicita al usuario que ingrese dos números.
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")

# Se verifica si alguno de los números ingresados está vacío, lo que indicaría que el usuario no ingresó un número.
if not num1 or not num2:
    # Si alguno de los números está vacío, se imprime un mensaje de error.
    print("Error, debe ingresar ambos numeros")
else:
    # Si ambos números fueron ingresados, se convierten a punto flotante para permitir la división.
    num1 = float(num1)
    num2 = float(num2)

    # Se verifica si el divisor es cero, lo que causaría un error en la división.
    if num2 == 0:
        # Si el divisor es cero, se imprime un mensaje de error.
        print("Error, el divisor no puede ser cero")
    else:
        # Si no hay errores, se realiza la división y se imprime el resultado.
        resultado = num1 / num2
        print(f"El resultado de la division es: {resultado}")
