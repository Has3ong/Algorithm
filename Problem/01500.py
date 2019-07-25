def solution():
    A, B = map(int, input().split(' '))

    division = A % B
    num = A // B

    arr = [num] * B
    for i in range(division):
        arr[i] += 1

    ret = 1
    for i in arr:
        ret *= i
    print(ret)


solution()