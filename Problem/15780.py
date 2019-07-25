def solution():
    N, K = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))

    res = sum(arr) - K

    if res >= N:
        print('YES')
    else:
        print('NO')
solution()