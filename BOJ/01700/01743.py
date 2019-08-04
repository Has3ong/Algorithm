import sys
from queue import Queue

def bfs(Q, Map, Check, N, M):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    index = 0
    while (not Q.empty()):
        x, y = Q.get()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx and 0 <= ny and nx < N and ny < M):
                if (Check[nx][ny] == False and Map[nx][ny] > 0):
                    Check[nx][ny] = True
                    Q.put((nx, ny))
                    index += 1
    return index

def solution():
    N, M, K = map(int, input().split(' '))

    Map = [[0] * M for _ in range(N)]
    Check = [[False] * M for _ in range(N)]

    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split(' '))

        Map[X-1][Y-1] = 1

    Q = Queue()
    ret = []
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 1 and Check[i][j] == False:
                Q.put((i, j))
                ret.append(bfs(Q, Map, Check, N, M))

    print(max(ret))

solution()