"""
Escribe un programa que clasifique una lista de edades en diferentes
categorías: niño (0-12), adolescente (13-17)
adulto (18-64) y mayor (65+).
"""

# Lista de edades
edades = [3, 15, 18, 25, 70, 10, 50, 67]

# Diccionario para clasificar las edades
clasificacion = {
    "niño": [],
    "adolescente": [],
    "adulto": [],
    "mayor": []
}

# Clasificar las edades
for edad in edades:
    if edad <= 12:
        clasificacion["niño"].append(edad)
    elif edad <= 17:
        clasificacion["adolescente"].append(edad)
    elif edad <= 64:
        clasificacion["adulto"].append(edad)
    else:
        clasificacion["mayor"].append(edad)

# Imprimir la clasificación de edades
print("Clasificación de edades:", clasificacion)
