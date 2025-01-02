"""
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""
def fizzbuzz(n):
    for n in range(1, 100+1):
        if n % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
        elif n % 3 == 0:
            return 'Fizz'
        elif n % 5 == 0:
            return 'Buzz'
        else:
            return n


print(fizzbuzz())