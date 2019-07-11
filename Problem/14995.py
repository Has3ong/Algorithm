def solution():
    N = int(input())
    fibo = [0, 1, 1, 1]

    if N < 4:
        print(fibo[N])
        return

    for i in range(4, N+1):
        fibo.append(fibo[i-1] + fibo[i-3])
    print(fibo[N])
solution()