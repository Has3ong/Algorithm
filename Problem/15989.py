def solution():
    T = int(input())

    dp = [0] * 10001
    dp[0] = 1

    for i in range(1, 4):
        for j in range(1, 10001):
            if (j - i) >= 0:
                dp[j] += dp[j - i]

    for i in range(T):
        N = int(input())
        print(dp[N])
solution()
