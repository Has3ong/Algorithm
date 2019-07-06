def solution():
    Table = [False] * 361
    N, K = map(int, input().split(' '))
    CY = list(map(int, input().split(' ')))
    HW = list(map(int, input().split(' ')))

    Table[0] = True

    for i in range(N):
        degree = CY[i]
        for j in range(360):
            if not Table[j]:
                continue

            for k in range(1, 360):
                Table[(j + k * degree) % 360] = True
                Table[(360 * 360 + j - k * degree) % 360] = True

    for i in range(K):
        if Table[HW[i]]:
            print('YES')
        else:
            print('NO')

solution()