"""
Enunciado: Escribe una función para cada operación matemática básica
(suma, resta, multiplicación, división) y permite al usuario elegir la operación y los números.
"""

# Función para sumar dos números
def suma(a, b):
    return a + b

# Función para restar el segundo número del primero
def resta(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir el primer número por el segundo, con verificación para evitar división por cero
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "División por cero no permitida"

# Bucle principal que se ejecuta hasta que el usuario elija salir
while True:
    # Mostrar el menú de operaciones disponibles
    print("\nElija la operacion: \n1.-Suma \n2.-Resta \n3.-Multiplicar \n4.-Dividir \n5.-Salir")
    opcion = int(input("Ingrese la opcion: "))  # Leer la opción elegida por el usuario
    
    # Verificar si la opción está dentro del rango permitido
    if 1 <= opcion <= 5:
        # Si el usuario elige salir, terminar el bucle
        if opcion == 5:
            print("Gracias por usar el programa")
            break
        
        # Si la opción es una operación matemática, solicitar los números
        if opcion in [1, 2, 3, 4]:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            
            # Ejecutar la operación correspondiente y mostrar el resultado
            if opcion == 1:
                print(f"La suma de {a} y {b} es: {suma(a, b)}")
            elif opcion == 2:
                print(f"La resta de {a} y {b} es: {resta(a, b)}")
            elif opcion == 3:
                print(f"La multiplicacion de {a} y {b} es: {multiplicar(a, b)}")
            elif opcion == 4:
                print(f"La division de {a} y {b} es: {division(a, b)}")
    else:
        # Si la opción no es válida, mostrar un mensaje de error
        print("Opcion no valida.")
