def solution():
    positionX = [0] * 1000
    positionY = [0] * 1000
    x1, y1 = map(int, input().split(' '))
    x2, y2 = map(int, input().split(' '))
    x3, y3 = map(int, input().split(' '))

    positionX[x1] += 1
    positionY[y1] += 1
    positionX[x2] += 1
    positionY[y2] += 1
    positionX[x3] += 1
    positionY[y3] += 1

    A = 0
    B = 0

    if positionX[x1] == 1:
        A = x1
    elif positionX[x2] == 1:
        A = x2
    else:
        A = x3

    if positionY[y1] == 1:
        B = y1
    elif positionY[y2] == 1:
        B = y2
    else:
        B = y3

    print(A, B)

solution()