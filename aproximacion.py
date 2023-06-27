objetivo = int(input('Escoge un numero: '))  # Solicita al usuario que ingrese un número y lo guarda en la variable objetivo.
epsilon = 0.0001  # Define un valor pequeño para epsilon, que determina la precisión de la aproximación.
paso = epsilon**2  # Calcula el tamaño del paso utilizado en cada iteración para acercarse a la raíz cuadrada.
respuesta = 0.0  # Inicializa la variable respuesta con el valor 0.0.

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    # El ciclo se ejecuta mientras la diferencia entre el cuadrado de la respuesta y el objetivo sea mayor o igual a epsilon,
    # y mientras la respuesta sea menor o igual al objetivo.
    print(abs(respuesta**2 - objetivo), respuesta)  # Imprime la diferencia entre el cuadrado de la respuesta y el objetivo, junto con el valor actual de respuesta.
    respuesta += paso  # Incrementa la respuesta en el tamaño del paso en cada iteración.

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')  # Si la diferencia entre el cuadrado de la respuesta y el objetivo sigue siendo mayor o igual a epsilon, se imprime un mensaje indicando que no se encontró la raíz cuadrada.
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')  # Si la diferencia entre el cuadrado de la respuesta y el objetivo es menor que epsilon, se imprime la raíz cuadrada encontrada.
