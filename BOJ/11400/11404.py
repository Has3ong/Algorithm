import sys

def solution():
    _INF = 1000001
    N = int(input())
    T = int(input())
    Floyd = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j :
                Floyd[i][j] = 0
            else:
                Floyd[i][j] = _INF

    for i in range(T):
        x, y, distance = map(int,sys.stdin.readline().split())
        Floyd[x-1][y-1] = min(Floyd[x-1][y-1], distance)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                Floyd[i][j] = min(Floyd[i][j], Floyd[i][k] + Floyd[k][j])


    for i in range(N):
        ret = ''
        for j in range(N):
            if Floyd[i][j] == _INF:
                ret += '0'
                ret += ' '
            else:
                ret += str(Floyd[i][j])
                ret += ' '
        print(ret)


solution()