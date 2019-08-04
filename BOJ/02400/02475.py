def solution():
    arr = list(map(int, input().split(' ')))

    temp = 0
    for i in arr:
        temp += i * i

    print(temp % 10)


solution()