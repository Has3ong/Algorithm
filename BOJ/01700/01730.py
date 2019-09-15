def solution():
    N = int(input())
    move = str(input())

    picture = [[0] * N for _ in range(N)]

    x, y = 0, 0

    for i in range(len(move)):
        if move[i] == 'U':
            if y - 1 < 0: continue
            picture[y][x] |= 1
            picture[y - 1][x] |= 1
            y -= 1
        elif move[i] == 'D':
            if y + 1 >= N: continue
            picture[y][x] |= 1
            picture[y + 1][x] |= 1
            y += 1
        elif move[i] == 'L':
            if x - 1 < 0: continue
            picture[y][x] |= 2
            picture[y][x - 1] |= 2
            x -= 1
        elif move[i] == 'R':
            if x + 1 >= N: continue
            picture[y][x] |= 2
            picture[y][x + 1] |= 2
            x += 1
        else:
            pass

    for i in range(N):
        for j in range(N):
            if picture[i][j] == 0:
                picture[i][j] = '.'
            elif picture[i][j] == 1:
                picture[i][j] = '|'
            elif picture[i][j] == 2:
                picture[i][j] = '-'
            elif picture[i][j] == 3:
                picture[i][j] = '+'
            else: pass

    for i in range(N):
        ret = ''
        for j in range(N):
            ret += picture[i][j]
        print(ret)
solution()