def solution():
    CHECK = [False, False] + [True] * 10000001
    Primes = []

    for i in range(2, 10000001):
        if CHECK[i]:
            Primes.append(i)
            for j in range(2 * i, 10000001, i):
                CHECK[j] = False

    N = int(input())


    for i in Primes:
        if N % i == 0:
            while N % i == 0:
                N //= i
                print(i)

solution()