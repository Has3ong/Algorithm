def solution():
    x1, y1 = map(int, input().split(' '))
    x2, y2 = map(int, input().split(' '))
    x3, y3 = map(int, input().split(' '))

    if (y3 - y2) / (x3 - x2) == (y2 - y1) / (x2 - x1):

        print('WHERE IS MY CHICKEN?')
    else:
        print('WINNER WINNER CHICKEN DINNER!')

solution()