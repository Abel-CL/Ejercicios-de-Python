'''
Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante)
y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.
'''

# Solicitar la contraseña al usuario
key1 = input('Ingrese su contraseña: ')
key2 = input('Ingrese nuevamente su contraseña: ')

# Establecer el límite de intentos
limite = 3
# Inicializar el contador de intentos
contador = 1

# Mientras las contraseñas no coincidan y no se haya alcanzado el límite de intentos
while key1 != key2 and contador < limite:
    print('Las contraseñas no son iguales')
    # Solicitar nuevamente la confirmación de la contraseña
    key2 = input('Confirme su contraseña: ')
    # Incrementar el contador de intentos
    contador += 1
    
# Verificar si las contraseñas coinciden
if key1 == key2:
    print('Contraseñas correctas')
else:
    print('Se han agotado los intentos')
