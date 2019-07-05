def solution():
    A, M = map(int, input().split(' '))
    res = M
    for i in range(1, M):
        if A * i % M == 1:
            res = min(res, i)
    print(res)
solution()