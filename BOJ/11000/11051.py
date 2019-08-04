def solution():
    N, K = map(int, input().split(' '))

    dp = [[0] * 1002 for _ in range(1002)]

    for i in range(1002):
        for j in range(i):
            if j == 0:
                dp[i][j] = 1
            elif j == i - 1 :
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print(dp[N+1][K] % 10007)

solution()