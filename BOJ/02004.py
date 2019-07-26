def solution():
    N, M = map(int, input().split(' '))

    cnt2 = 0
    cnt5 = 0
    temp = 1
    while temp <= N:
        temp *= 2
        cnt2 += N // temp

    temp = 1
    while temp <= M:
        temp *= 2
        cnt2 -= M // temp

    temp = 1
    while temp <= N - M:
        temp *= 2
        cnt2 -= (N-M) // temp

    temp = 1
    while temp <= N:
        temp *= 5
        cnt5 += N // temp

    temp = 1
    while temp <= M:
        temp *= 5
        cnt5 -= M // temp

    temp = 1
    while temp <= N-M:
        temp *= 5
        cnt5 -= (N-M) // temp

    print(min(cnt2, cnt5))

solution()