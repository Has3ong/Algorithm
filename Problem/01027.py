def solution():
    N = int(input())
    A = list(map(int, input().split(' ')))
    B = [0] * N

    for i in range(N):
        e = -99999999999
        for j in range(i+1, N):
            d = (A[j] - A[i]) / (j - i)
            if d > e:
                e = d
                B[i] += 1
                B[j] += 1
    res = 0
    for i in B:
        res = max(res, i)
    print(res)

solution()