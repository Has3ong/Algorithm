def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a
def solution():
    N, M = map(int, input().split(' '))

    print(M - gcd(N, M))
solution()