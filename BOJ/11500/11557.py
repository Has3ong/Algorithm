def solution():
    T = int(input())

    for i in range(T):

        _max = 0
        _school = ''

        N = int(input())
        for j in range(N):
            A, B = map(str, input().split(' '))
            if int(B) > _max:
                _max = int(B)
                _school = A
        print(_school)

solution()
