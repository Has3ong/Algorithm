dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
cnt = 0

for y in range(1900, 2001):
    for m in range(12):
        day = dayList[m]
        if y % 4 == 0 and m == 1:
            day += 1
        for d in range(day):
            if y > 1900 and d == 0 and total % 7 == 6:
                cnt += 1
            total += 1

print(cnt)