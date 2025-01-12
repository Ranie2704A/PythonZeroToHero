def number(n):
    aux = ""
    for i in range(1, n + 1):
        aux += str(i)

    print(aux)


if __name__ == '__main__':
    n = int(input())
    number(n)
