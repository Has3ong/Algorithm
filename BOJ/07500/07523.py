import sys

def solution():
    N = int(input())
    for i in range(N):
        A, B = map(int, sys.stdin.readline().split())

        if A < 0:
            resA = (abs(A) * abs(A + 1)) // 2 * -1 + A
        else:
            resA = ((A * (A + 1)) // 2 - A) * -1

        if B < 0:
            resB = (abs(B) * abs(B + 1)) // 2
        else:
            resB = (B * (B + 1)) // 2

        print('Scenario #%d:' %(i+1))
        print(resB + resA)
        print()

solution( )