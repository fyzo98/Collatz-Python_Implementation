def collatz(number):
    """
    Esta función implementa la conjetura de Collatz, también conocida como la conjetura 3n+1.
    La conjetura dice que para cualquier número entero positivo, la secuencia terminará en 1.

    Parámetros:
    number (int): el número entero positivo inicial para la secuencia de Collatz.

    Returns:
    None. Imprime la secuencia de Collatz para el número dado.
    """
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1

        print(str(number))

while True:
    """
    Este bucle solicita al usuario que introduzca un número entero.
    Si el valor introducido no es un número entero, se imprime un mensaje de error y se vuelve a solicitar la entrada.
    Si el valor introducido es un número entero, se ejecuta la función collatz y se rompe el bucle.
    """
    try:
        collatz(int(input('Introduce un número: \n')))
        break
    except ValueError:
        print('Debes introducir un número entero.')
