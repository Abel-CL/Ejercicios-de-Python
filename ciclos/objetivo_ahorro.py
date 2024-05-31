"""
Diseña un programa que permita al usuario establecer un objetivo de ahorro en bolivianos
y luego ingresar cantidades adicionales de dinero hasta alcanzar o superar dicho objetivo.
El programa mostrará un mensaje indicando si se logró el objetivo y el monto total ahorrado.
"""

# Preguntar al usuario cuál es el objetivo de ahorro en bolivianos
alcancia = float(input('¿Cuántos bolivianos quiere ahorrar?: '))
# Inicializar el monto ahorrado en 0
ahorro = 0.0

# Mientras el monto ahorrado sea menor que el objetivo, seguir pidiendo montos para ahorrar
while ahorro < alcancia:
    monto = float(input('¿Cuántos bolivianos quiere meter en la alcancía?: '))
    # Sumar el monto ingresado al total ahorrado
    ahorro += monto

    # Comprobar si se ha alcanzado exactamente el objetivo
    if ahorro == alcancia:
        print('¡Objetivo conseguido!')
    # Comprobar si se ha superado el objetivo
    elif ahorro > alcancia:
        print('¡Se ha superado el objetivo!')
        print('El monto final es:', ahorro)

# Imprimir el monto final ahorrado
print('El monto final es:', ahorro)
