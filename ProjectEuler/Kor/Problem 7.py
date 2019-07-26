CHECK = [False, False] + [True] * 1000000
Primes = []

for i in range(2, 1000000):
    if CHECK[i]:
        Primes.append(i)
        for j in range(2 * i, 1000000, i):
            CHECK[j] = False
print(Primes[10000])