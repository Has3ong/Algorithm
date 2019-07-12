import sys
def solution():
    N, M = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + arr[i-1]

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if a == 1:
            print(dp[b])
        else:
            print(dp[b] - dp[a - 1])
solution()