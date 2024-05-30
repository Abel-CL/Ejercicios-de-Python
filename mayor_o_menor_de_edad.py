"""
determina la edad de una persona y verifica si es menor o mayor de edad considerando 18 la edad de adulto.
"""

edad_adulta = 18

edad = int(input("Ingrese su edad: "))

if edad >= edad_adulta:
    print(f"La persona con edad {edad} es un adulto")
else:
    print(f"La persona con edad {edad} es menor de edad")