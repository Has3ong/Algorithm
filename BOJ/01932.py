def solution():
    T = int(input())
    Field = []
    for i in range(T):
        nums = list(map(int, input().split(' ')))
        Field.append(nums)

    dp = [[0] * T for i in range(T)]
    dp[0][0] = Field[0][0]

    for i in range(1, T):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + Field[i][j]
            elif j > 0 and j < i:
                dp[i][j] = max(dp[i-1][j-1]+Field[i][j], dp[i-1][j] + Field[i][j])
            else:
                dp[i][j] = dp[i-1][j-1] + Field[i][j]
    print(max(dp[T-1]))
solution()