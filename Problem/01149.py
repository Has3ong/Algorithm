def solution():
    N = int(input())
    Field = []
    dp = [[0] * 3 for i in range(N)]

    for i in range(N):
        RGB = list(map(int, input().split(' ')))
        Field.append(RGB)

    for i in range(N):
        if i == 0:
            dp[i] = Field[i]
        else:
            dp[i][0] = Field[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = Field[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = Field[i][2] + min(dp[i-1][0], dp[i-1][1])
    print(min(dp[N-1]))
solution()