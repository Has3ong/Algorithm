def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def abs(x):
    if x > 0:
        return x
    else:
        return x * -1

def solution():
    N, M, K = map(int, input().split(' '))

    res = 0
    for i in range(N+1):
        for j in range(M+1):
            for k in range(N+1):
                for l in range(M+1):
                    if i == k and j == l:
                        continue
                    if i == k or j == l:
                        if K - 1 == abs(i - k) + abs(j - l):
                            res += 1
                            continue

                    g = gcd(abs(k - i), abs(j - l))
                    if g == 0:
                        continue

                    x = abs(k - i) // g
                    if x == 0:
                        continue

                    if abs(k - i) // x == K - 1:
                        res += 1

    print(res//2)
solution()