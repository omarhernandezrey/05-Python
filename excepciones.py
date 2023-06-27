def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]  # Divide cada elemento de la lista por el divisor
    except ZeroDivisionError as e:
        print(e)  # Imprime el mensaje de error si se produce una división por cero
        return lista  # Devuelve la lista original si se produce una excepción


lista = list(range(10))  # Crea una lista del 0 al 9
divisor = 0  # Define el divisor como cero

print(divide_elementos_de_lista(lista, divisor))  # Llama a la función e imprime el resultado