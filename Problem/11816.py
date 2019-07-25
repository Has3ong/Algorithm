def solution():
    _16 = '0123456789abcdef'
    _8 = '01234567'

    N = str(input())
    if N[0] == '0':
        if N[1] == 'x':
            res = 0
            mul = 1
            for i in range(len(N)-2):
                res += _16.index(N[len(N) - i - 1]) * mul
                mul *= 16
            print(res)

        else:
            res = 0
            mul = 1
            for i in range(len(N)-1):
                res += _8.index(N[len(N) - i - 1]) * mul
                mul *= 8
            print(res)
    else:
        print(N)
solution()