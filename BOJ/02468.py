from queue import Queue

def bfs(Field, Check, count, dx, dy, Height):
    q = Queue()
    q.put((dx, dy))
    count[0] = count[0] + 1
    Check[dx][dy] = 0

    while (not q.empty()):
        x, y = q.get()

        if x - 1 >= 0:
            if Check[x - 1][y] == 1 and Field[x - 1][y] > Height:
                q.put((x - 1, y))
                Check[x-1][y] = 0

        if y - 1 >= 0:
            if Check[x][y - 1] == 1 and Field[x][y - 1] > Height:
                q.put((x, y - 1))
                Check[x][y-1] = 0

        if x + 1 < len(Field):
            if Check[x + 1][y] == 1 and Field[x + 1][y] > Height:
                q.put((x + 1, y))
                Check[x+1][y] = 0

        if y + 1 < len(Field[0]):
            if Check[x][y + 1] == 1 and Field[x][y + 1] > Height:
                q.put((x, y + 1))
                Check[x][y+1] = 0

def solution():
    N = int(input())

    Field = []
    ret = 0

    for i in range(N):
        Field.append(list(map(int, input().split(' '))))

    _maxHeight = 0
    for i in range(N):
        _maxHeight = max(max(Field[i]), _maxHeight)

    for i in range(0, _maxHeight+1):
        count = [0]
        Check = [[1] * N for i in range(N)]
        for j in range(N):
            for k in range(N):
                if Field[j][k] <= i:
                    Check[j][k] == 0

        for j in range(N):
            for k in range(N):
                if Check[j][k] == 1 and Field[j][k] > i:
                    bfs(Field, Check, count, j, k, i)
        ret = max(ret, count[0])

    print(ret)

solution()