import math
def solution():
    arr = list(map(int, input().split(' ')))

    X = math.sqrt((arr[0] * arr[0]) - (arr[1] * arr[1]))
    Y = math.sqrt((arr[0] * arr[0]) - (arr[2] * arr[2]))
    Z = ((X * Y) - (arr[1] * arr[2])) / arr[0]

    if Z < 0:
        print(-1)
    else:
        print(round(Z))
solution()