def solution():
    T = int(input())

    dp = [0, 1, 2, 4]

    for i in range(T):
        N = int(input())
        for j in range(4, N + 1):
            dp.insert(j, dp[j - 1] + dp[j - 2] + dp[j - 3])
        print(dp[N])


solution()