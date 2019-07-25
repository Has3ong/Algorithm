
def solution():
    mod = 15746
    dp = [0, 1, 2]

    N = int(input())

    for i in range(3, N+1):
        dp.append((dp[i-1] + dp[i-2]) % mod)
    print(dp[N])
solution()