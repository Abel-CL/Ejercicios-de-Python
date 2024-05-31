'''
Los alumnos de un curso se han divido en dos  grupos A y B de acuerdo al sexo
y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M
y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
pantalla el grupo que le corresponde.
'''

# Solicitar nombre y sexo al usuario
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ")

# Convertir el nombre a mayúsculas para comparaciones más simples
nombre = nombre.upper()

# Comprobar a qué grupo pertenece el usuario
if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    # Si es mujer y su nombre está antes de la 'M' o es hombre y su nombre está después de la 'N', pertenece al grupo A.
    grupo = "A"
else:
    # En caso contrario, pertenece al grupo B.
    grupo = "B"

# Mostrar el grupo correspondiente
print("Usted pertenece al grupo", grupo)
