def solution():
    while 1:
        a, b = map(int, input().split(' '))
        if a == 0 and b == 0:
            return
        print(a + b)


solution()