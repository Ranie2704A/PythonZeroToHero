def up_score(n, arr):
    arr.sort(reverse=True)

    first_highest = arr[0]
    second_highest = None

    for i in range(1, n):
        if arr[i] < first_highest:
            second_highest = arr[i]
            break

    return second_highest


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(up_score(n, arr))