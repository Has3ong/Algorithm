def solution():
    N = int(input())
    cnt = 0
    while N > 9:
        number = N
        temp = 1
        while number:
            temp *= number % 10
            number //= 10
        N = temp
        cnt += 1
    print(cnt)
solution()