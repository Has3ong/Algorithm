def solution():
    N, T = map(int, input().split(' '))
    work = list(map(int, input().split(' ')))

    total = 0
    count = 0
    for i in work:
        if total + i > T:
            break

        total += i
        count += 1
    print(count)
solution()