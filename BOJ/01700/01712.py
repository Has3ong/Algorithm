def solution():
    A, B, C = map(int, input().split(' '))

    if B >= C:
        print('-1')
        return

    print((A // (C-B)) + 1)

solution()