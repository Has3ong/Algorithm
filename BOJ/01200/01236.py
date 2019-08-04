def solution():
    X, Y = map(int, input().split(' '))

    Castle = []
    Check = [[0] * 51 for _ in range(2)]
    for i in range(X):
        Castle.append(list(input()))

    for i in range(X):
        for j in range(Y):
            if Castle[i][j] == 'X':
                Check[1][i] += 1
                Check[0][j] += 1

    x = 0
    y = 0
    for i in range(51):
        if Check[1][i] > 0:
            x += 1
        if Check[0][i] > 0:
            y += 1

    print(max(X - x, Y - y))
solution()