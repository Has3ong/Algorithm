import math
def fact(n):
    a = 1
    for i in range(1, n+1):
        a = a * i
    return a

def solution():
    X, Y = map(int, input().split(' '))

    distance = Y - X
    i = 1
    while i * i < distance:
        i = i + 1

    if distance < (i * i) - i + 1:
        print(2 * i - 2)
    else:
        print(2 * i - 1)

T = int(input())
for i in range(T):
    solution()