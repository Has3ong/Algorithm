def getCount(n, bool):
    if bool:
        n = n // 2
    return n

def solution():
    N, M, K = map(int, input().split(' '))
    res = 0

    while K > 0:
        if N // 2 >= M:
            N -= 1
        else:
            M -= 1
        K -= 1

    if N // 2 <= M:
        res = N // 2
    else :
        res = M
    print(res)

solution()