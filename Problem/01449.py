def solution():
    N, L = map(int, input().split(' '))
    WATER = (list(map(int, input().split(' '))))

    wCheck = [False] * 1001

    for i in WATER:
        wCheck[i] = True

    cnt = 0
    for i in range(1001):
        if wCheck[i]:
            wCheck[i] = False
            cnt += 1
            for j in range(L):
                if i + j >= 1001:
                    continue
                wCheck[i+j] = False

    print(cnt)
solution()