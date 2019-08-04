def solution():
    CHECK = [False, False] + [True] * 1000001
    Primes = []

    for i in range(2, 1000001):
        if CHECK[i]:
            Primes.append(i)
            for j in range(2 * i, 1000001, i):
                CHECK[j] = False

    T = int(input())
    for i in range(T):
        N = int(input())
        flag = 0
        for j in Primes:
            if j and N % j == 0:
                flag = 1
                break
        if flag:
            print("NO")
        else:
            print("YES")
solution( )