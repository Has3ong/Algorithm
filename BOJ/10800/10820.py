def solution():
    a = 'abcdefghijklmnopqrstuvwxyz'
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '1234567890'

    for i in range(100):
        try:
            B = str(input())

        except EOFError:
            break

        ret = 0
        ret1 = 0
        ret2 = 0
        ret3 = 0

        for j in range(len(B)):
            if B[j].isalpha():
                if B[j] in a:
                    ret += 1
                else:
                    ret1 += 1

            if B[j].isnumeric():
                ret2 += 1
            if B[j].isspace():
                ret3 += 1

        print(ret, ret1, ret2, ret3)


solution()