"""
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
cortando el ingreso de datos cuando el usuario ingrese el monto 0.
Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar,
informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
"""

# Inicializar el total y el descuento en 0
total = 0
descuento = 0

# Solicita al usuario ingresar el monto de la primera compra
compra = float(input("Ingrese el monto de su compra (0 para terminar): "))

# Bucle que se ejecuta mientras el monto de la compra sea diferente de cero
while compra != 0:
    if compra < 0:
        # Mensaje de error para valores negativos
        print("Error! No se permiten valores negativos.")
    else:
        # Suma el monto de la compra al total
        total += compra
    # Solicita al usuario ingresar el monto de la siguiente compra
    compra = float(input("Por favor, ingrese el monto de la compra (0 para terminar): "))

# Verifica si el total de las compras supera los $1000 y calcula el descuento si es necesario
if total > 1000:
    descuento = total * 0.1
    total -= descuento

# Imprime el total de las compras y un mensaje sobre el descuento si corresponde
print("El total de sus compras es de bs", total)
if descuento > 0:
    print("Gracias a su preferencia, usted obtendrá un descuento del 10% por haber gastado más de bs 1000.")
