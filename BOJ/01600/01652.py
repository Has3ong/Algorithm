def solution():
    N = int(input())
    MAP = []
    for i in range(N):
        MAP.append(list(str(input())))

    width = 0
    height = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if MAP[i][j] == '.':
                cnt += 1
            else :
                cnt = 0

            if cnt == 2:
                width += 1

    for i in range(N):
        cnt = 0
        for j in range(N):
            if MAP[j][i] == '.':
                cnt += 1
            else :
                cnt = 0

            if cnt == 2:
                height += 1

    print(width, height)

solution()