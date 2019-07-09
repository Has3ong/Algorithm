def solution():
    N = int(input())
    dp = [0, 1, 2]
    index = 0
    while 1:
        if index <= 2:
            index += 1
            continue
        if index > N:
            print(dp[N] % 10007)
            break
        dp.insert(index, dp[index-1] + dp[index-2])
        index += 1
solution()