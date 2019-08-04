def reverse(n):
    a = 0
    while n:
        a *= 10
        a += n % 10
        n //= 10
    return a

def isSame(a, b):
    if a == reverse(b):
        return True
    else:
        return False

def solution():
    N = int(input())
    for i in range(N):
        a = int(input())
        b = reverse(a)

        if isSame(a+b, a+b):
            print('YES')
        else:
            print('NO')


solution()