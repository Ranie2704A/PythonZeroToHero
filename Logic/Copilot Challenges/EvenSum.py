
def even_sum(n : int) -> int:
    sum = 0

    for i in range(0 , n+1):
        if i % 2 == 0:
            sum += i

    return sum

print(even_sum(4))