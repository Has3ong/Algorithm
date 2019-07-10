def solution():
    Check = [False] * 1001
    N, M = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))

    for i in arr:
        for j in range((N // i)+1):
            Check[i*j] = True

    ret = 0
    for i in range(N+1):
        if Check[i]:
            ret += i
    print(ret)
solution()