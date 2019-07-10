def solution():
    N, M = map(int, input().split(' '))
    result = N

    while N >= M:
        N //= M
        result += N
    print(result)


solution()