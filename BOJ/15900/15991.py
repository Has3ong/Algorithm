
def solution():
    mod = 1000000009
    dp1 = [0] * 100001
    dp2 = [0] * 100001
    dp1[0] = 1

    for i in range(1, 100001):
        for j in range(1, 4):
            if i - j >= 0:
                dp1[i] += dp1[i-j] % mod
                dp1[i] %= mod

    for i in range(1, 100001):
        if i % 2 == 0:
            dp2[i] = dp1[i//2]
            if i - 2 >= 0:
                dp2[i] += dp1[(i - 2) // 2]
            dp2[i] %= mod

        else:
            for j in range(1, 4):
                if j == 2:
                    continue
                if i - j >= 0:
                    dp2[i] += dp1[(i - j) // 2]
                    dp2[i] %= mod

    T = int(input())
    for i in range(T):
        N = int(input())
        print(dp2[N])

solution()