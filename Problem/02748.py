def solution():
    N = int(input())
    Fib = [0, 1, 1]
    for i in range(3, N+1):
        Fib.append(Fib[i-1] + Fib[i-2])
    print(Fib[N])
solution()