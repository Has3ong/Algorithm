def solution():
    N = int(input())
    size = list(map(int, input().split(' ')))
    cluster = int(input())

    ret = 0
    cnt = 0
    for i in range(N):
        if size[i] == 0:
            pass
        if size[i] % cluster:
            cnt += 1
        cnt += size[i] // cluster

    ret = cnt * cluster
    print(ret)
solution()
