import sys
def solution():
    N = int(input())

    for i in range(N):
        X, Y = map(int, sys.stdin.readline().split(' '))
        print('You get %d piece(s) and your dad gets %d piece(s).' %(X//Y, X%Y))
solution()