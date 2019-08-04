def solution():
    while 1:
        N = int(input())
        if N == 0:
            break

        temp = 11
        while temp >= 10:
            temp = 0
            while N > 0:
                temp += N % 10
                N //= 10
            N = temp
        print(temp)

solution()