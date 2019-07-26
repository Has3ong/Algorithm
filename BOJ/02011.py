dp = [0] * 5001
_MOD = 1000000

def solution():
    N = str(input())
    dp[0] = 1
    dp[1] = 1

    if N[0] == '0':
        print(0)
        return

    for i in range(2, len(N) + 1):
        step1 = int(N[i - 1])
        step2 = int(N[i - 2]) * 10 + int(N[i - 1])

        if step1 >= 1 and step1 <= 9:
            dp[i] = dp[i] + dp[i-1]

        if step2 >= 10 and step2 <= 26:
            dp[i] = dp[i] + dp[i-2]

        dp[i] %= _MOD
    print(dp[len(N)])

solution()