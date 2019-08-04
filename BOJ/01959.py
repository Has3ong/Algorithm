def solution():
    M, N = map(int, input().split(' '))

    if M >= N:
        if N == 1:
            print(0)
            print(M, 1)
        else:
            if M != N:
                print((N - 1) * 2 + 1)
            else:
                print((N - 1) * 2)

            if N % 2:
                print(M - (N // 2), (N + 1) // 2)
            else:
                print((N // 2) + 1, (N + 1) // 2)

    else:
        if M == 1:
            print(0)
            print(1, N)
        else:
            print((M - 1) * 2)
            if M % 2:
                print((M + 1) // 2, N - (M // 2))
            else:
                print((M // 2) + 1, (M + 1) // 2)

solution()