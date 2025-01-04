
number = int(input("Please provide a number: "))

if 0 < number <= 50:
    for i in range(1, number + 1):
        print(i)
    print(f"I've printed until {number}!")
else:
    print("The number is not between 1 and 50")


"""
IA's version
while True:
    try:
        number = int(input("Please provide a number between 1 and 50: "))
        if 0 < number <= 50:
            for i in range(1, number + 1):
                print(i)
            print(f"I've printed until {number}!")
            break  # Salir del bucle una vez que el número es válido
        else:
            print("The number is not between 1 and 50. Try again.")
    except ValueError:
        print("That's not a valid number. Please try again.")


"""