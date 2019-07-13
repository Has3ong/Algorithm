import sys
sys.setrecursionlimit(10000000)
memo = {}
def dp(C, O, L, A):
    if 2 <= L: return 0
    if 3 <= A: return 0

    if O == C:
        return 1
    if (O, L, A) in memo:
        return memo[(O, L, A)]

    memo[(O, L, A)] = dp(C, O + 1, L, 0) + dp(C, O +1, L +1, 0) + dp(C, O +1, L, A + 1)
    return memo[(O, L, A)]

def solution():
    N = int(input())
    print(dp(N, 0, 0, 0) % 1000000)

solution()
