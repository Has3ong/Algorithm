def solution():
    A, B, C = map(int,input().split(' '))

    ret = 1
    x = A % C
    while B > 0:
        if B % 2 :
            ret *= x
            ret %= C
        x *= x
        x %= C
        B //= 2

    print(ret)
solution()