def solution():
    N = int(input())
    dp = [0] * (N+1)
    index = 0

    while 1:
        temp = 1000001
        if index > N:
            break
        if index <= 1:
            dp[index] = 0
        else:
            if index % 3 == 0:
                temp = min(temp, dp[index//3])
            if index % 2 == 0:
                temp = min(temp, dp[index//2])
            temp = min(temp, dp[index-1])
            dp[index] = temp+1
        index += 1
    print(dp[N])
solution()