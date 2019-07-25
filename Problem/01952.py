def solution():
    N, M = map(int, input().split(' '))

    flag = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 0
    j = 0

    Field = [[-1] * M for _ in range(N)]
    Field[0][0] = 1

    res = 0
    d = 0
    while d < (N * M) - 1:
        if j + dy[flag] < M and j + dy[flag] > -1 and i + dx[flag] < N and i + dx[flag] > -1:
            if Field[i + dx[flag]][j + dy[flag]] == -1:
                i += dx[flag]
                j += dy[flag]
                Field[i][j] = 1
                d += 1
            else:
                flag = (flag + 1) % 4
                Field[i][j] = 10
                res += 1
        else:
            flag = (flag + 1) % 4
            Field[i][j] = 10
            res += 1
    print(res)

solution()