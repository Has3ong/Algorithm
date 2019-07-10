def solution():
    dp = [1, 1]
    N = int(input())

    if N < 2:
        print(dp[N])
    else:
        for i in range(2, N+1):
            dp.append((dp[i-1] + dp[i-2] + 1) % 1000000007)
        print(dp[N])
solution()