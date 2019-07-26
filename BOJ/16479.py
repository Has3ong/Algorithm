def solution():
    Z = int(input())
    r1, r2 = map(int, input().split(' '))

    x = (r1 - r2)/2
    ret = 0
    ret = (Z * Z) - (x * x)
    print(ret)
solution()