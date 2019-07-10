def _1038(N, SUM, ARR, RES):
    if N == -1:
        RES.append(SUM)
        return

    _1038(N - 1, SUM, ARR, RES)
    _1038(N - 1, (SUM * 10) + N, ARR, RES)


def solution():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []

    N = int(input())

    if N >= 1023:
        print('-1')
        return

    _1038(9, 0, arr, res)

    res.sort()
    print(res[N + 1])


solution()