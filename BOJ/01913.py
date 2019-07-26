def solution():
    N = int(input())
    Find = int(input())

    Field = [[-1] * N for _ in range(N)]
    Field[0][0] = N * N

    i = 0
    j = 0
    # 상 2 하 0 좌 3 우 1
    flag = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    d = N * N - 1
    res = ''
    while 1:
        if d == 0:
            break

        if i + dy[flag] < N and i + dy[flag] > -1 and j + dx[flag] < N and j + dy[flag] > -1:
            if Field[i + dy[flag]][j + dx[flag]] == -1:
                i += dy[flag]
                j += dx[flag]
                Field[i][j] = d
                if d == Find:
                    res += str(i + 1) + ' ' + str(j + 1)
                d -= 1
            else:
                flag = (flag + 1) % 4
        else:
            flag = (flag + 1) % 4

    for i in range(N):
        string = ''
        for j in range(N):
            string += str(Field[i][j]) + ' '
        print(string)

    if N * N == Find:
        print('1 1')
        return
    print(res)


solution()