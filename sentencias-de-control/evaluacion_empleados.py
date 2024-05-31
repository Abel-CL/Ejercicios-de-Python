"""
En una empresa determinada, sus empleados sonn evaluados al final de cada ano.
Los puntos que pueden obtener en la evaluacion comienzan en 0.0 y pueden ir aumentando,
traduciendose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o mas,
pero no valores intermedios entre las cifras mencionadas.
A continuacion se muestra una tabla con los niveles correspondientes a cada puntuacion.
La cantidad de dinero conseguida en cada nivel es de 2.400 bs multiplicada  por el numero de niveles alcanzado.

NIVEL               PUNTUACION
Inaceptable -----------0.0
Aceptable -------------0.4
Meritorio -------------0.6 o mas

Escribir un programa que lea la puntuacion del usuario e indique su nivel de rendimiento,
asi como la cantidad de dinero que resivira el usuario.
"""

# Definir las variables para los niveles y la bonificación
bonificacion = 2400
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6

# Solicitar al usuario que ingrese la puntuación obtenida
puntos = float(input('Ingrese la puntuacion obtenida por el usuario: '))

# Determinar el nivel de rendimiento y la cantidad de dinero que recibirá el usuario
if puntos == inaceptable:
    print ('El nivel es Inaceptable')
elif puntos == aceptable:
    print ('El nivel es Aceptable')
elif puntos >= meritorio:
    print ('El nivel es Meritorio')
else:
    print ("Error! La puntuacion ingresada no corresponde a ningun nivel.")

ganancia = puntos * bonificacion

# Mostrar la cantidad de dinero que recibirá el usuario
print(f'Te corresponde cobrar  {ganancia} bs')
