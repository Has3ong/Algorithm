def solution():
    N = int(input())

    _MOD = 1000000
    T = _MOD // 10 * 15

    Fibonacci = [0] * T
    Fibonacci[1] = 1

    for i in range(2, T):
        Fibonacci[i] = (Fibonacci[i-1] + Fibonacci[i-2]) % _MOD

    print(Fibonacci[N % T])
solution()