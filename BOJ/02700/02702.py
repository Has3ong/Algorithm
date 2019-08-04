def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def solution():
    T = int(input())
    for i in range(T):
        A, B = map(int, input().split(' '))
        print((A * B) // gcd(B, A), gcd(B, A))

solution()
