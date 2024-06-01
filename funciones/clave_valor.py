"""
Escribe una función que reciba un número variable de argumentos y devuelva su suma.
Luego, crea otra función que acepte argumentos de llave-valor e imprima las llaves y valores.
"""

# Definir una función que recibe un número variable de argumentos y devuelve su suma
def suma(*args):
    return sum(args)

# Definir una función que acepta argumentos de llave-valor e imprime las llaves y valores
def imprimir_llaves_valores(**kwargs):
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")

# Ejemplo de uso de la función suma
print(f"La suma de 1, 2, 3 es: {suma(1, 2, 3)}")

# Ejemplo de uso de la función imprimir_llaves_valores
imprimir_llaves_valores(nombre="Juan", edad=30, ciudad="Madrid")
