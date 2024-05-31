"""
Enunciado: Crea un diccionario que almacene nombres y números de teléfono. Permite al usuario agregar, eliminar, buscar y listar contactos.
"""

contactos = {}

while True:
    print("\nElige una accion: \n1.-agregar \n2.-eliminar \n3.-buscar \n4.-listar \n5.-salir ")
    accion = input("Ingrese la accion: ").lower()
    if accion == "agregar":
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        if len(telefono) == 8 and telefono[0] == "7":
            contactos[nombre] = telefono
            print(f"Contacto {nombre} agregado.")
        else:
            print("El numero de telefono debe tener 8 digitos y empezar con un 7.")
    elif accion == "eliminar":
        nombre = input("Nombre: ")
        if nombre in contactos:
            del contactos[nombre]
            print(f"Contacto de {nombre} eliminado.")
        else:
            print(f"El contacto de {nombre} no existe.")
    elif accion == "buscar":
        nombre = input("Nombre: ")
        if nombre in contactos:
            print(f"El telefono es: {contactos[nombre]}")
        else:
            print(f"El contacto de {nombre} no existe.")
    elif accion == "listar":
        for nombre, telefono in contactos.items():
            print(f"Nombre: {nombre} \nTelefono: {telefono}")
    elif accion == 'salir':
        break
    else:
        print("Acción no reconocida.")
