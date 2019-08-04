def solution():
    T = int(input())
    CHECK = [False, False] + [True] * 10000000
    Primes = []

    for i in range(2, 10000000):
        if CHECK[i]:
            Primes.append(i)
            for j in range(2 * i, 10000000, i):
                CHECK[j] = False
    print(Primes[T-1])
solution()