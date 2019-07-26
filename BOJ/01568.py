def solution():
    N = int(input())
    cnt = 0
    k = 1

    while N > 0:
        if k > N:
            k = 1
        N -= k
        cnt += 1
        k += 1
    print(cnt)
solution()