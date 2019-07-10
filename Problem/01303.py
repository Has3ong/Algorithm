from queue import Queue

def BFS(Q, miro, Check, N, M, Color):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    index = 0
    while (not Q.empty()):
        x, y = Q.get()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx and 0 <= ny and nx < M and ny < N):
                if (Check[nx][ny] == False and miro[nx][ny] == Color):
                    Check[nx][ny] = True
                    Q.put((nx, ny))
                    index += 1

    if index == 0:
        return 1
    else :
        return (index * index)

def solution():
    Q = Queue()
    N, M = map(int, input().split(' '))

    miro = []
    Check = [[False] * N for i in range(M)]
    temp = []

    for i in range(M):
        miro.append(list(str(input())))
    W = 0
    B = 0
    for i in range(M):
        for j in range(N):
            if miro[i][j] == 'W' and Check[i][j] == False:
                Q.put((i, j))
                W += BFS(Q, miro, Check, N, M, 'W')

            elif miro[i][j] == 'B' and Check[i][j] == False:
                Q.put((i, j))
                B += BFS(Q, miro, Check, N, M, 'B')

    print(W, B)

solution()