"""
Imaginemos que en nuestra tienda hay una carné por puntos y que alguien debe pagar el precio_final_de_compra.
Si tienes menos de 100 puntos realizaremos un descuento del 10%. Si es mayor a 100 y menor a 150 aplicamos un 12%.
Si tienes 150 un 15% y sino, el resto de los casos de más de 150, un 20%. ¡Crea la variable puntos y juega con ella!
"""

# Definir la variable puntos (puedes cambiar este valor para probar diferentes escenarios)
puntos = 120

# Definir el precio final de compra (supongamos que es $100)
precio_final_de_compra = 100

# Determinar el porcentaje de descuento según la cantidad de puntos
if puntos < 100:
    descuento_porcentaje = 0.1  # 10%
elif puntos < 150:
    descuento_porcentaje = 0.12  # 12%
elif puntos == 150:
    descuento_porcentaje = 0.15  # 15%
else:
    descuento_porcentaje = 0.20  # 20%

# Calcular el precio final de compra con el descuento aplicado
precio_final_con_descuento = precio_final_de_compra * (1 - descuento_porcentaje)

# Imprimir el resultado
print(f'Con {puntos} puntos, el precio final de compra con descuento es: ${precio_final_con_descuento:.2f}')
