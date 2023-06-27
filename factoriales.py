def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    returns n!
    """
    print(n)  # Imprime el valor actual de n.

    if n == 1:  # Verifica si n es igual a 1, en cuyo caso retorna 1, terminando la recursión.
        return 1

    return n * factorial(n - 1)  # Realiza la llamada recursiva a la función factorial, multiplicando n por el factorial de n-1.

n = int(input('Escribe un entero: '))  # Solicita al usuario que ingrese un número entero.
print(factorial(n))  # Imprime el resultado del factorial de n llamando a la función factorial con el número ingresado.