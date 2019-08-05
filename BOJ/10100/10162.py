def solution():
    N = int(input())
    A, B, C = 0, 0, 0

    if N % 10:
        print(-1)
        return

    while N > 0 :
        if N >= 300:
            A += N // 300
            N %= 300
            continue
        if N >= 60:
            B += 1
            N -= 60
            continue
        if N >= 10:
            C += 1
            N -= 10

    print(A, B, C)

solution()