def solution():
    T = int(input())
    for i in range(T):
        ret = 0

        Car = int(input())
        ret += Car

        T2 = int(input())

        for j in range(T2):
            A, B = map(int, input().split(' '))
            ret += A * B
        print(ret)
solution()