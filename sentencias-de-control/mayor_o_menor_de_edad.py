"""
determina la edad de una persona y verifica si es menor o mayor de edad considerando 18 la edad de adulto.
"""

# Define la edad adulta como 18 años.
edad_adulta = 18

# Solicita al usuario que ingrese su edad y la convierte a un entero.
edad = int(input("Ingrese su edad: "))

# Comprueba si la edad ingresada es mayor o igual a la edad considerada adulta.
if edad >= edad_adulta:
    # Imprime un mensaje indicando que la persona es un adulto.
    print(f"La persona con edad {edad} es un adulto")
else:
    # Imprime un mensaje indicando que la persona es menor de edad.
    print(f"La persona con edad {edad} es menor de edad")
