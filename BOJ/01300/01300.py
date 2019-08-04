def getCount(x, N):
    count = 0

    for i in range(1, N+1):
        count += min(x // i, N)

    return count

def solution():
    N = int(input())
    K = int(input())

    left = 1
    right = N * N
    mid = 0
    ret = 0

    while left <= right:
        mid = (left + right) // 2
        cnt = getCount(mid, N)

        if cnt >= K:
            ret = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ret)

solution()