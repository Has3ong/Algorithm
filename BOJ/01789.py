import math

def solution():
    S = int(input())
    N = 0
    N = int(math.sqrt(S*2))

    while ((N * N) + N) > (S * 2):
        N -= 1

    print(int(N))

solution()