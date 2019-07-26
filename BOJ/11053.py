def solution():
    N = int(input())
    dp = [0] * (N)
    A = list(map(int, input().split(' ')))

    for i in range(0, N):
        min = 0
        for j in range(0, i):
            if A[i] > A[j] :
                if min < dp[j]:
                    min = dp[j]
        dp[i] = min + 1

    print(max(dp))

solution()