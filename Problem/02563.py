import sys
def solution():
    white = [[0] * 101 for _ in range(101)]

    T = int(input())
    for i in range(T):
        X, Y = map(int, sys.stdin.readline().split())

        for j in range(X, X+10):
            for k in range(Y, Y+10):
                white[j][k] += 1

    ret = 0
    for i in range(101):
        for j in range(101):
            if white[i][j] != 0:
                ret += 1
    print(ret)

solution()
