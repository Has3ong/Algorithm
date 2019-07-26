def solution():
    N = int(input())
    fibo = [0, 1]
    mod = 1000000000
    for i in range(2, 1000001):
        fibo.append((fibo[i-1] + fibo[i-2]) % mod)

    if N == 0:
        print(0)
        print(0)

    elif N > 0:
        print(1)
        print(fibo[N])

    else:
        if (N * -1) % 2 == 1:
            print(1)
        else:
            print(-1)
        print(fibo[N*(-1)])
solution()