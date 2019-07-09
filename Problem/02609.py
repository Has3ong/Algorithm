def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def solution():
    A, B = map(int, input().split(' '))
    print(gcd(A,B))
    print( (A*B)//gcd(A,B) )

solution()