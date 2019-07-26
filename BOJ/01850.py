def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def solution():
    A, B = map(int, input().split(' '))

    X = gcd(A, B)

    ret = ''
    for i in range(X):
        ret += '1'
    print(ret)
solution()