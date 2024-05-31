"""
Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t),
el programa tiene que pedir entonces la base y la altura y escribir el área.
Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c),
el programa tiene que pedir entonces el radio y escribir el área.

Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo es:
Pi (aproximadamente 3,141592) por el radio al cuadrado.

Nota: Utilice como valor de pi el valor 3.141592.
"""

# Se imprime un mensaje de bienvenida y se muestra el menú de opciones para elegir la figura geométrica.
print('\nCALCULO DE AREAS\nElija una figura geometrica: \na) Triangulo \nb) Circulo')

# Se solicita al usuario que ingrese la figura geométrica que desea calcular (T para triángulo, C para círculo).
area = input('¿Qué figura quiere calcular (Escriba T o C)?')

# Se utiliza una estructura condicional para determinar el cálculo a realizar.
if area == 'T' or area == 't':
    # Si el usuario elige calcular el área de un triángulo, se solicitan la base y la altura.
    base = float(input('Escriba la base: '))
    altura = float(input('Escriba la altura: '))
    # Se calcula el área del triángulo usando la fórmula (base * altura) / 2.
    area = ((base * altura) / 2)
    # Se muestra el resultado del cálculo, redondeado a dos decimales.
    print(f'\nEl área del triángulo es:  {round(area, 2)}')
elif area == 'C' or area == 'c':
    # Si el usuario elige calcular el área de un círculo, se solicita el radio.
    PI = 3.141592
    radio = float(input('Escriba el radio: '))
    # Se calcula el área del círculo usando la fórmula π * radio^2.
    area = PI * (radio ** 2)
    # Se muestra el resultado del cálculo, redondeado a dos decimales.
    print(f'\nEl área del círculo es:   {round(area, 2)}')
else:
    # Si el usuario ingresa una opción inválida, se muestra un mensaje de error.
    print("Error en la elección")
