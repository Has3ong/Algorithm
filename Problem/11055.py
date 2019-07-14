def solution():
    N = int(input())
    num = list(map(int, input().split(' ')))
    dp = [0] * N
    for i in range(N):
        dp[i] += num[i]
        for j in range(i):
            if num[j] < num[i] and dp[i] < dp[j] + num[i]:
                dp[i] = dp[j] + num[i]
    print(max(dp))
solution()