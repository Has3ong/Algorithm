def solution():
    N = int(input())
    arr = list(map(int, input().split(' ')))
    dp = [0] * N

    _MAX = 0
    for i in range(N):
        _MIN = 0
        for j in range(i):
            if arr[i] > arr[j]:
                if _MIN < dp[j]:
                    _MIN = dp[j]
        dp[i] = _MIN + 1
        if _MAX < dp[i]:
            _MAX = dp[i]
    print(max(dp))

solution()