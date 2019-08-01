def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def solution():
    N = int(input())

    for i in range(N):
        A, B = map(int, input().split(' '))
        print( (A*B)//gcd(A,B) )

solution()