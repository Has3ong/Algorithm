
def solution():
    N = int(input())
    M = int(input())

    mod = 1000000007

    N %= mod
    ans = 1
    cnt = 1
    while M > 0:
        if M % 2 == 1:
            ans *= N
            ans %= mod

        N *= N
        N %= mod

        M //= 2
    print(ans)

solution()
