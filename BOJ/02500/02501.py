def solution():
    N, K = map(int, input().split(' '))

    ret = []
    for i in range(1, (N // 2) + 1):
        if N % i == 0:
            ret.append(i)

    ret.append(N)

    if len(ret) < K:
        print(0)
        return
    print(ret[K - 1])
solution()