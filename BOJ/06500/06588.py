def solution():
    CHECK = [False, False] + [False] * 1000001

    for i in range(3, 1000001, 2):
        if CHECK[i//2]:
            continue
        for j in range(i * i, 1000001, i*2):
            CHECK[j // 2] = True

    while True:
        n = int(input())
        if n == 0:
            break
        for i in range(3, 1000001, 2):
            if not CHECK[i // 2] and not CHECK[(n-i) // 2]:
                print("%d = %d + %d" %(n, i, n-i))
                break

solution()