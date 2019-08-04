import sys
def solution():
    N = int(input())
    position = []
    for i in range(N):
        X, Y = map(int, sys.stdin.readline().split())
        position.append((Y, X))

    position.sort()
    for i in range(N):
        print('%d %d' %(position[i][1], position[i][0]))

solution()