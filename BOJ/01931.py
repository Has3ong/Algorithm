import sys
def solution():
    N = int(input())

    field = []

    for i in range(N):
        S, E = map(int, sys.stdin.readline().split())
        field.append((S, E))

    field = sorted(field, key=lambda time: time[0])
    field = sorted(field, key=lambda time: time[1])

    now = 0
    res = 0

    for i in field:
        if now <= i[0]:
            now = i[1]
            res += 1
    print(res)
solution()