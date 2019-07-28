def solution():
    N = int(input())

    for i in range(N):
        T = int(input())

        ret1 = 0
        ret2 = 0

        for j in range(T):
            A, B = map(float, input().split(' '))
            ret1 += A
            ret2 += A * B
        print('%d %0.1f' %(ret1, ret2/ret1))

solution()