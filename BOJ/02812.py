from collections import deque


def _2812(x, dq):
    while len(dq) and dq[-1] < x:
        dq.pop()
    dq.append(x)


def solution():
    N, K = map(int, input().split(' '))
    number = list(str(input()))

    dq = deque()
    ret = []
    for i in range(K):
        _2812(number[i], dq)

    for i in range(K, N):
        _2812(number[i], dq)
        ret.append(dq[0])
        dq.popleft()

    for i in ret:
        print(i, end='')


solution()