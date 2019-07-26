def Check(r, c, R, C):
    return r < 0 or r >= R or c < 0 or c >= C

def solution():
    R, C = map(int, input().split(' '))

    arrD1 = [[-1] * 770 for i in range(770)]
    arrD2 = [[-1] * 770 for i in range(770)]
    arrD3 = [[-1] * 770 for i in range(770)]
    arrD4 = [[-1] * 770 for i in range(770)]

    Map = []
    for i in range(R):
        Map.append(list(str(input())))


    for d in range(R + C + 1):
        for c in range(C):
            r = d - c
            if Check(r, c, R, C):
                continue
            if Check(r + 1, c - 1, R, C):
                arrD3[r][c] = (Map[r][c] == '1')
            else:
                arrD3[r][c] = (Map[r][c] == '1') * (arrD3[r+1][c-1] +1)

        for r in range(R):
            c = d - r
            if Check(r, c, R, C):
                continue
            if Check(r - 1, c + 1, R, C):
                arrD1[r][c] = (Map[r][c] == '1')
            else:
                arrD1[r][c] = (Map[r][c] == '1') * (arrD1[r-1][c+1] +1)

    for d in range(1-C, R):
        for r in range(R):
            c = r - d
            if Check(r, c, R, C):
                continue
            if Check(r - 1, c - 1, R, C):
                arrD4[r][c] = (Map[r][c] == '1')
            else:
                arrD4[r][c] = (Map[r][c] == '1') * (arrD4[r-1][c-1] +1)

        for r in range(R-1, -1, -1):
            c = r - d
            if Check(r, c, R, C):
                continue
            if Check(r + 1, c + 1, R, C):
                arrD2[r][c] = (Map[r][c] == '1')
            else:
                arrD2[r][c] = (Map[r][c] == '1') * (arrD2[r+1][c+1] +1)

    MAX = 0
    for r in range(R):
        for c in range(C):
            maxPoint = min(arrD1[r][c], arrD2[r][c])
            if maxPoint < MAX:
                continue
            for i in range(maxPoint, 0, -1):
                if (c + 2 * (i - 1) >= C):
                    continue
                if (i < MAX):
                    break
                if min(arrD3[r][c+2*(i-1)], arrD4[r][c+2*(i-1)]) >= i:
                    MAX = max(MAX, i)
                    break
    print(MAX)

solution()
