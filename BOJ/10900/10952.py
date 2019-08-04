def solution():
    while 1:
        A, B = map(int, input().split(' '))
        if A == 0 and B == 0:
            return
        print(A+B)

solution()
