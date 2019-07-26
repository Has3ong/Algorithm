from queue import Queue

def bfs(Field, Check, count, dx, dy):
    q = Queue()
    q.put((dx, dy))
    count[0] = count[0] + 1
    Check[dx][dy] = 1

    while (not q.empty()):
        x, y = q.get()

        if x - 1 >= 0:
            if Check[x - 1][y] == 0 and Field[x - 1][y] == 1:
                q.put((x - 1, y))
                Check[x-1][y] = 1

        if y - 1 >= 0:
            if Check[x][y - 1] == 0 and Field[x][y - 1] == 1:
                q.put((x, y - 1))
                Check[x][y-1] = 1

        if x + 1 < len(Field):
            if Check[x + 1][y] == 0 and Field[x + 1][y] == 1:
                q.put((x + 1, y))
                Check[x+1][y] = 1

        if y + 1 < len(Field[0]):
            if Check[x][y + 1] == 0 and Field[x][y + 1] == 1:
                q.put((x, y + 1))
                Check[x][y+1] = 1

def solution():
    M, N, K = map(int, input().split(' '))

    Field = [[0] * N for i in range(M)]
    Check = [[0] * N for i in range(M)]
    count = [0]

    for i in range(K):
        X, Y = map(int, input().split(' '))
        Field[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if Check[i][j] == 0 and Field[i][j] == 1:
                bfs(Field, Check, count, i, j)

    print(count[0])

T = int(input())

for i in range(T):
    solution()