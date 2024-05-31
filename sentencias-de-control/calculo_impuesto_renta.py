"""
Los tramos de impuestos para la declaración de la renta en un determinado país son los siguientes:

RENTA                        IMPUESTO
Menos de 1000 bs -------------- 5%
Entre  1000 bs y 2000 bs ------ 15%
Entre 2000 bs y 3500 bs ------- 20%
Entre  3500 bs y 6000 bs ------ 30%
Mas de 6000 bs ---------------- 45%

Escribe un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo de impuesto que le corresponde.
"""

# Solicitar renta anual al usuario
renta = input('Ingrese su renta anual en bs: ')

# Convertir la renta a un número decimal
renta = float(renta)

# Determinar el tipo de impuesto según la renta anual
if renta < 1000:
    tipo_impuesto = "5%"
elif renta < 2000:
    tipo_impuesto = "15%"
elif renta < 3500:
    tipo_impuesto = "20%"
elif renta < 6000:
    tipo_impuesto = "30%"
else:
    tipo_impuesto = "45%"

# Calcular el impuesto a pagar
impuesto = renta * float(tipo_impuesto.strip('%')) / 100

# Mostrar el tipo de impuesto y el monto a pagar
print(f'Tiene que pagar un impuesto del {tipo_impuesto} sobre su renta anual, lo que equivale a {impuesto} bs')
