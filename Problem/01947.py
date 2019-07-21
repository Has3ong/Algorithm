def solution():
    N = int(input())
    dp = [0] * 1000002
    mod = 1000000000

    for i in range(2, 1000001):
        if i == 2:
            dp[i] = 1
        else:
            dp[i] = ((i - 1) * (dp[i-1] + dp[i-2])) % mod
    print(dp[N])

solution()