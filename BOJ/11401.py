def Mul(x, y, mod):
    ret = 1
    while y > 0:
        if y % 2 != 0:
            ret *= x
            ret %= mod
        x *= x
        x %= mod
        y //= 2
    return ret


def solution():
    N, K = map(int, input().split(' '))
    mod = 1000000007
    T1 = 1
    T2 = 1

    for i in range(1, N + 1):
        T1 *= i
        T1 %= mod
    for i in range(1, K + 1):
        T2 *= i
        T2 %= mod
    for i in range(1, N - K + 1):
        T2 *= i
        T2 %= mod

    T3 = Mul(T2, mod - 2, mod)
    T3 %= mod

    print((T1 * T3) % mod)


solution()