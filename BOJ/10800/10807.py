def solution():
    N = int(input())
    arr = list(map(int, input().split(' ')))
    K = int(input())

    cnt = 0

    for i in arr:
        if i == K:
            cnt += 1
    print(cnt)
solution()