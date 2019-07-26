CHECK = [False, False] + [True] * 2000000

SUM = 0
for i in range(2, 2000000):
    if CHECK[i]:
        SUM += i
        for j in range(2 * i, 2000000, i):
            CHECK[j] = False

print(SUM)