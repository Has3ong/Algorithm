def solution():
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split(' '))

        print(1 + (N - M) * M)


solution()