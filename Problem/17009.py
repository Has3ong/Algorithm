def solution():
    B1 = int(input())
    B2 = int(input())
    B3 = int(input())

    T1 = int(input())
    T2 = int(input())
    T3 = int(input())

    if B1 * 3 + B2 * 2 + B3 > T1 * 3 + T2 * 2 + T3:
        print('A')
    elif B1 * 3 + B2 * 2 + B3 < T1 * 3 + T2 * 2 + T3:
        print('B')
    else:
        print('T')


solution()