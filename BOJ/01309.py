def solution():
    N = int(input())
    dp = [0, 3, 7]

    if N <= 2:
        print(dp[N])
        return

    for i in range(2, N):
        dp.append((dp[i] * 2 + dp[i-1]) % 9901)
    print(dp[N])
solution()
