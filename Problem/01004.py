import math


def solution():
    x1, y1, x2, y2 = map(int, input().split(' '))

    N = int(input())
    count = 0
    for i in range(N):
        px, py, pr = map(int, input().split(' '))

        s_distance = math.sqrt((x1 - px) ** 2 + (y1 - py) ** 2) - pr
        e_distance = math.sqrt((x2 - px) ** 2 + (y2 - py) ** 2) - pr

        if (s_distance * e_distance) < 0:
            count += 1
    print(count)


T = int(input())

for i in range(T):
    solution()