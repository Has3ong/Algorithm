def solution():
    T = int(input())
    _A = 350.34
    _B = 230.90
    _C = 190.55
    _D = 125.30
    _E = 180.90

    for i in range(T):
        res = 0.0
        A, B, C, D, E = map(int, input().split(' '))

        res += (A * _A) + (B * _B) + (C * _C) + (D * _D) + (E * _E)
        print('$%0.2f' %res)

solution()
