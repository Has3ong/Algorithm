def solution():
    dp = [[0] * 4 for _ in range(100001)]
    mod = 1000000009
    N = int(input())

    dp[0] = [0, 0, 0, 0]
    dp[1] = [0, 1, 0, 0]
    dp[2] = [0, 0, 1, 0]
    dp[3] = [0, 1, 1, 1]

    for i in range(4, 100001):
        dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % mod
        dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % mod
        dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % mod

    for i in range(N):
        A = int(input())
        print(sum(dp[A]) % mod)


solution()