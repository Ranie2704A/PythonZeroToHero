def square_of(n):
    aux = 0
    if n < 0:
        print(f"The number {n} is not an non-negative integer")
    else:
        for i in range(0, n):
            aux = i ** 2
            print(aux)


if __name__ == '__main__':
    n = int(input())

    square_of(n)