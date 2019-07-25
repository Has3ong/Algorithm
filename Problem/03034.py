import math
def solution():
    N, W, H = map(int, input().split(' '))

    a = int(math.sqrt(W * W + H * H) + 1)
    for i in range(N):
        X = int(input())
        if X < a:
            print('DA')
        else:
            print('NE')
solution()