def opciones():
    print(f'Opciones para hallar raiz cuadrada \n (1) Enumeracion exhaustiva \n (2) Aproximacion de soluciones \n (3) Busqueda binaria')
    opcion = int(input('Elija una opcion: '))  # Solicita al usuario que elija una opción.
    numero = int(input('Elija un numero: '))  # Solicita al usuario que elija un número.
  
    if opcion == 1:
        Enumeracion(numero)  # Si la opción es 1, llama a la función Enumeracion con el número ingresado.
    elif opcion == 2:
        Aproximacion(numero)  # Si la opción es 2, llama a la función Aproximacion con el número ingresado.
    elif opcion == 3:
        BusquedaBinaria(numero)  # Si la opción es 3, llama a la función BusquedaBinaria con el número ingresado.
    else:
        print('Elija 1, 2 o 3')  # Si la opción no es válida, imprime un mensaje indicando que se debe elegir una opción válida.

def Enumeracion(objetivo):
    respuesta = 0
    

    while respuesta**2 < objetivo:
        print(respuesta)  # Imprime el valor actual de respuesta.
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')  # Si el cuadrado de respuesta es igual al objetivo, imprime la raíz cuadrada exacta.
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')  # Si no se cumple la condición anterior, indica que el objetivo no tiene una raíz cuadrada exacta.

def Aproximacion(objetivo):
    epsilon = 0.001  # Define un valor pequeño para epsilon, que determina la precisión de la aproximación.
    paso = epsilon**2  # Calcula el tamaño del paso utilizado en cada iteración para acercarse a la raíz cuadrada.
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso  # Incrementa la respuesta en el tamaño del paso en cada iteración.

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')  # Si la diferencia entre el cuadrado de la respuesta y el objetivo sigue siendo mayor o igual a epsilon, indica que no se encontró la raíz cuadrada.
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')  # Si la diferencia entre el cuadrado de la respuesta y el objetivo es menor que epsilon, imprime la raíz cuadrada encontrada.

def BusquedaBinaria(objetivo):
    epsilon = 0.001  # Define un valor pequeño para epsilon, que determina la precisión de la aproximación.
    bajo = 0.0  # Inicializa el límite inferior del rango de búsqueda en 0.0.
    alto = max(1.0, objetivo)  # Inicializa el límite superior del rango de búsqueda en el máximo entre 1.0 y el objetivo.
    respuesta = (alto + bajo) / 2  # Calcula una respuesta inicial como el punto medio del rango de búsqueda.

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')  # Imprime los límites bajo y alto del rango de búsqueda, junto con el valor actual de respuesta.

        if respuesta**2 < objetivo:
            bajo = respuesta  # Si el cuadrado de la respuesta es menor que el objetivo, actualiza el límite inferior del rango de búsqueda.
        else:
            alto = respuesta  # Si el cuadrado de la respuesta es mayor o igual al objetivo, actualiza el límite superior del rango de búsqueda.

        respuesta = (alto + bajo) / 2  # Actualiza la respuesta como el punto medio del nuevo rango de búsqueda.

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')  # Imprime la raíz cuadrada encontrada.

opciones()  # Llama a la función opciones para mostrar las opciones y realizar la ejecución según la opción elegida.