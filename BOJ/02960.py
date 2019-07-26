def solution():
    N, K = map(int, input().split(' '))
    CHECK = [False] * (N + 1)

    cnt = 0
    for i in range(2, N+1):
        if CHECK[i]:
            continue

        for j in range(i, N+1, i):
            if CHECK[j] :
                continue
            cnt += 1
            CHECK[j] = True

            if cnt == K:
                print(j)
                return

solution()