"""
Escribe un programa para una empresa que tiene salas de juego para las edades y quiere calcular
de forma automatica el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario  la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 anos puede entrar gratis,  si tiene entre 4 y 18 anos
debe pagar 5 bs y si es mayor de 18 anos  debe pagar 10 bs.
"""

# Solicitar al usuario que ingrese su edad
edad = input('¿Cuál es su edad? ')

# Convertir la edad ingresada a un número entero
edad = int(edad)

# Determinar el precio de la entrada basado en la edad del cliente
if edad < 4:
    # Si el cliente tiene menos de 4 años, la entrada es gratuita
    print('La entrada es gratuita')
elif edad < 18:
    # Si el cliente tiene entre 4 y 18 años, el precio de la entrada es de 5 Bs.
    print('El precio de la entrada es de 5 Bs.')
else:
    # Si el cliente tiene 18 años o más, el precio de la entrada es de 10 Bs.
    print('El precio de la entrada es de 10 Bs.')
