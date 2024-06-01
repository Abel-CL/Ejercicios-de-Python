"""
Escribe una función recursiva que calcule la potencia de un número (base y exponente ingresados por el usuario).
"""

# Definir una función recursiva para calcular la potencia de un número
def potencia(base, exponente):
    # Caso base: cualquier número elevado a la 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: multiplicar la base por el resultado de la función con el exponente disminuido en 1
    else:
        return base * potencia(base, exponente - 1)

# Solicitar la base al usuario
base = float(input("Ingresa la base: "))

# Solicitar el exponente al usuario
exponente = int(input("Ingresa el exponente: "))

# Calcular y mostrar el resultado de la potencia
print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")
