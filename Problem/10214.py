def solution():
    T = int(input())
    for i in range(T):
        K = 0
        Y = 0
        for j in range(9):
            A, B = map(int, input().split(' '))
            Y += A
            K += B

        if Y > K:
            print('Yonsei')
        elif Y < K:
            print('Korea')
        else:
            print('Draw')


solution()