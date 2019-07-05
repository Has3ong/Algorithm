def solution():
    E, S, M = map(int, input().split(' '))
    result = 0
    year = 1

    while 1:
        if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
            result = year
            break
        year += 1
    print(result)
solution()