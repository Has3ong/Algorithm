def solution():
    N = int(input())
    mod = 1000000007
    a = 0
    b = 1

    if N == 0:
        print(0)
        return

    if N == 1:
        print(1)
        return

    for i in range(2, N+1):
        c = (a+b) % mod
        a = b
        b = c
    print(c)
solution()