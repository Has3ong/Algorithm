def printgcd(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def solution():
    N = int(input())
    if N == 2:
        a, b = map(int, input().split(' '))
        printgcd(gcd(a,b))
    else:
        a, b, c = map(int, input().split(' '))
        printgcd(gcd(gcd(a, b), c))
solution()