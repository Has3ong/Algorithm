import sys
def solution():
    _MAX = 1025
    N, M = map(int, input().split(' '))
    Field = []
    for i in range(N):
        Field.append(list(map(int, input().split(' '))))

    dp = [[0] * (_MAX) for _ in range (_MAX)]
    dp[0][0] = Field[0][0]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + Field[i][0]
        dp[0][i] = dp[0][i-1] + Field[0][i]

    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] + Field[i][j] - dp[i-1][j-1]

    for i in range(M):
        x, y, X, Y = map(int, sys.stdin.readline().split())
        print(dp[X-1][Y-1] + dp[x-2][y-2] - dp[X-1][y-2] - dp[x-2][Y-1])

solution()