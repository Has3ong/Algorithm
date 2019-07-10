def solution():
    N = int(input())
    F = int(input())

    N = (N // 100) * 100

    for i in range(100):
        M = N + i
        if M % F == 0:
            break

    print(str(M)[-2:])
solution()