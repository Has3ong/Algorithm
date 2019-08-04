def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def solution():
    N = int(input())
    for i in range(N):
        a, b = map(int, input().split(' '))

        print((a * b)//gcd(a, b))
solution()