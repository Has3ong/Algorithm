def solution():
    CHECK = [False, False] + [True] * 1000001
    Primes = []

    for i in range(2, 1000001):
        if CHECK[i]:
            Primes.append(i)
            for j in range(2 * i, 1000001, i):
                CHECK[j] = False

    N, M = map(int, input().split(' '))
    string = ""
    for i in range(N, M+1):
        if CHECK[i]:
            print(i)

solution()