"""
La pizzeria Bella Napoli ofrece pizzas vegetarianas y no  vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuacion.

Ingredientes Vegetarianos: Pimiento y tofu.
Ingredientes No vegetarianos: Peperoni, Jamon y Salmon.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en funcion de su respuesta le muestre un menu con los ingredientes disponibles para que elija.
Solo se puede elegir un ingrediente ademas de la mozzarella y el tomate que estan en todas las pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

# Se imprime un mensaje de bienvenida al usuario.
print('Bienvenido a Bella Napoli')

# Se muestra el menú de opciones para elegir el tipo de pizza.
print('\nTipo de pizzas disponibles:\n1-Vegetariana.\n2-No vegetariana.\n')

# Se solicita al usuario que ingrese el número de la pizza que desea.
pizza = int(input('Ingrese el numero de pizza que desea : '))

# Se utiliza una estructura condicional para determinar la elección del usuario.
if pizza == 1:
    # Si el usuario elige la pizza vegetariana, se muestra el menú de ingredientes disponibles.
    print('\nIngredientes Disponibles:\n1-Pimiento.\n2-Tofu.\n')
    # Se solicita al usuario que ingrese el número del ingrediente que desea agregar a su pizza.
    ingrediente = int(input('\nIngrese el numero del ingrediente que desee agregar a su pizza: '))
    # Se utiliza otra estructura condicional para determinar el ingrediente seleccionado por el usuario.
    if ingrediente == 1:
        # Se muestra un mensaje confirmando la elección del usuario.
        print('\nSu pizza es vegetariana de mozzarella, tomate y Pimiento.\n')
    elif ingrediente == 2:
        print('\nSu pizza es vegetariana de mozzarella, tomate y Tofu.\n')
    else:
        # Si el usuario ingresa un número de ingrediente inválido, se muestra un mensaje de error.
        print('\nError! Ingrese una opcion valida.\n')
elif pizza == 2:
    # Si el usuario elige la pizza no vegetariana, se muestra el menú de ingredientes disponibles.
    print('\nIngredientes Disponibles:\n1-Peperoni.\n2-Jamon.\n3-Salmon.\n')
    # Se solicita al usuario que ingrese el número del ingrediente que desea agregar a su pizza.
    ingrediente = int(input('\nIngrese el numero del ingrediente que desee agregar a su pizza: '))
    # Se utiliza otra estructura condicional para determinar el ingrediente seleccionado por el usuario.
    if ingrediente == 1:
        # Se muestra un mensaje confirmando la elección del usuario.
        print('\nSu pizza es no vegetariana de mozzarella, tomate y Peperoni.\n')
    elif ingrediente == 2:
        print('\nSu pizza es no vegetariana de mozzarella, tomate y Jamon.\n')
    elif ingrediente == 3:
        print('\nSu pizza es no vegetariana de mozzarella, tomate y Salmón.\n')
    else:
        # Si el usuario ingresa un número de ingrediente inválido, se muestra un mensaje de error.
        print('\nError! Ingrese una opción válida.\n')
else:
    # Si el usuario ingresa un número de pizza inválido, se muestra un mensaje de error.
    print('\nError! Ingrese una opción válida.\n')