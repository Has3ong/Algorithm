import sys
def solution():
    A = int(input())

    _A = 0
    _B = 0
    for i in range(A):
        X, Y = map(int, sys.stdin.readline().split(' '))
        if X > Y:
            _A += 1
        elif X < Y:
            _B += 1

    print(_A, _B)
solution()