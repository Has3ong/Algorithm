def solution():
    C, K, P = map(int, input().split(' '))

    res = 0
    for i in range(C+1):
        res += (K * i) + (P * (i * i))
    print(res)
solution()