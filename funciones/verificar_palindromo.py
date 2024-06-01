"""
Escribe una función que determine si una palabra ingresada es un palíndromo (se lee igual de adelante hacia atrás).
"""

# Definir la función que verifica si una palabra es un palíndromo
def palindromo(texto):
    # Remover espacios y convertir la palabra a minúsculas
    texto = texto.replace(" ", "").lower()
    # Comparar la palabra con su reverso
    return texto == texto[::-1]

# Bucle para solicitar palabras al usuario
while True:
    # Solicitar al usuario ingresar una palabra
    palabra = input("Ingrese la palabra: ")
    # Verificar si la palabra es 'fin' para terminar el programa
    if palabra.lower() == 'fin':
        print("Fin del programa")
        break
    # Verificar si la palabra es un palíndromo y mostrar el resultado
    if palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo")
