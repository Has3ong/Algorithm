def solution():
    N = int(input())
    stone = [0] * 1001

    stone[1] = 1
    stone[3] = 1
    stone[4] = 1

    for i in range(5, 1001):
        if not (stone[i-1] and stone[i-3] and stone[i-4]) :
            stone[i] = 1

    if stone[N]:
        print('SK')
    else:
        print('CY')
solution()