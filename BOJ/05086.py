def solution():
    while 1:
        A, B = map(int, input().split(' '))

        if A == 0 and B == 0:
            break

        if A > B:
            if A % B == 0:
                print('multiple')
            else:
                print('neither')
        else:
            if B % A == 0:
                print('factor')
            else:
                print('neither')


solution()