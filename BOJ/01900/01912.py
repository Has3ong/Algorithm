def solution():
    T = int(input())
    num = [0]
    num += list(map(int, input().split(' ')))
    dp = [0] * (T+1)

    result = -1001

    for i in range(1, T+1):
        dp[i] = max(dp[i-1] + num[i], num[i])
        result = max(result, dp[i])

    print(result)

solution()