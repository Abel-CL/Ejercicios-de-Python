'''
Escriba un programa que pida los coeficientes de una ecuación de segundo grado (ax² + bx + c = 0) y escriba la solución.

Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, 
tener dos soluciones o que todos los números sean solución.
Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

Estos son algunos ejemplos de posibles respuestas 
(el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones).

a	b	c	Solución
1	-2	2	Sin solución real
2	-7	3	Dos soluciones: 0.5 y 3.0
1	2	1	Una solución: -1.0
0	0	5	Sin solución
0	0	0	Todos los números son solución

'''

# Se solicita al usuario que ingrese los coeficientes de la ecuación de segundo grado (ax² + bx + c = 0).
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# Se calcula el discriminante de la ecuación (d = b² - 4ac).
d = b**2 - 4*a*c

# Se utiliza una estructura condicional para determinar la solución de la ecuación.
if a == b == c == 0:
    # Si los coeficientes a, b y c son todos cero, todos los números son solución.
    print("Todos los números son solución")
elif d < 0:
    # Si el discriminante es menor que cero, la ecuación no tiene soluciones reales.
    print("Sin solución real")
elif d == 0:
    if a != 0:  # Verificar si 'a' es diferente de cero.
        # Si el discriminante es igual a cero y 'a' no es cero, la ecuación tiene una solución única.
        x = -b / (2 * a)
        print("Una solución:", x)
    else:
        # Si 'a' es cero, la ecuación no puede ser resuelta como una ecuación de segundo grado.
        print("La ecuación no puede ser resuelta porque el coeficiente cuadrático 'a' es cero.")
else:
    if a != 0:  # Verificar si 'a' es diferente de cero.
        # Si el discriminante es mayor que cero y 'a' no es cero, la ecuación tiene dos soluciones reales.
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("Dos soluciones:", x1, "y", x2)
    else:
        # Si 'a' es cero, la ecuación no puede ser resuelta como una ecuación de segundo grado.
        print("La ecuación no puede ser resuelta porque el coeficiente cuadrático 'a' es cero.")

