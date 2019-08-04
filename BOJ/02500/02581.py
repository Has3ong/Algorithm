def solution():
    CHECK = [False, False] + [True] * 10001
    Primes = []

    for i in range(2, 10001):
        if CHECK[i]:
            Primes.append(i)
            for j in range(2 * i, 10001, i):
                CHECK[j] = False

    M = int(input())
    N = int(input())

    min = 10001
    sum = 0
    for i in Primes:
        if i > N :
            break
        if i < min and i >= M:
            min = i

        if i >= M:
            sum += i
    if not min == 10001:
        print(sum)
        print(min)
    else:
        print(-1)


solution()