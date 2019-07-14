import math

def solution():
    A, B, C = map(int, input().split(' '))
    temp = math.sqrt((A*A) / (B*B + C*C))
    print(int(temp * B), int(temp * C))
solution()