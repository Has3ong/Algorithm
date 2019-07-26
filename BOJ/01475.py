import math

def solution():
    room = list(map(int, str(input())))

    k = range(9)
    v = [0] * len(k)
    num = dict(zip(k, v))
    for i in room:
        if (i == 6) | (i == 9):
            num[6] += 0.5
        else:
            num[i] += 1

    res = math.ceil(max(num.values()))
    print(res)
solution()