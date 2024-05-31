"""
Escriba un programa que pida los coeficientes de una ecuación de primer grado (ax + b = 0) y escriba la solución.

Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución.
Se recuerda que la fórmula de las soluciones es x = -b / a
"""

# Se solicita al usuario que ingrese los coeficientes de la ecuación de primer grado (ax + b = 0).
a = float(input('Ingrese el coeficiente a: '))
b = float(input('Ingrese el coeficiente b: '))

# Se utiliza una estructura condicional para determinar la solución de la ecuación.
if a == 0 and b == 0:
    # Si ambos coeficientes son cero, entonces todos los números son solución.
    print('Todos los números son solución')
elif a == 0:
    # Si el coeficiente 'a' es cero, la ecuación no es de primer grado y no se puede realizar la operación.
    print("No se puede realizar la operación, el coeficiente 'a' debe ser distinto de cero")
else:
    # Si 'a' no es cero, se calcula la solución utilizando la fórmula x = -b / a.
    x = -b / a
    print("La solución de la ecuación es x =", x)
