def solution():
    N = int(input())
    dp = [0] * 31
    dp[0] = 1
    dp[2] = 3

    if N % 2 != 0:
        print(0)
        return

    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(4, N+1, 2):
            if i - j < 0:
                break

            dp[i] = dp[i] + dp[i-j] * 2
    print(dp[N])

solution()