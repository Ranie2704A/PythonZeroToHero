"""
Pide al usuario que adivine un número entre 1 y 100.
Genera un número aleatorio entre 1 y 100.
Compara la adivinanza del usuario con el número generado y da pistas de si el número es mayor o menor.
Permite múltiples intentos hasta que el usuario adivine el número correcto.
Al final, muestra el número de intentos que tomó adivinar el número correcto.
"""

from random import randint

number = randint(1, 100)
attempts = 0

while True:
    user = int(input("Guess the number between 1 and 100: "))
    if user == number:
        print("You've guessed the number!")
        break
    elif user < number:
        print("The number is greater")
    else:
        print("The number is smaller")
    attempts += 1

print(f"You've guessed the number {number} in {attempts} attemps")