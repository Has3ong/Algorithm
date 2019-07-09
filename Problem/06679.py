def solution():
    for i in range(1000, 10000):
        ret = 0
        retTwo = 0
        retSix = 0

        temp = i
        while temp > 0:
            ret += temp % 10
            temp //= 10

        temp = i
        while temp > 0:
            retTwo += temp % 12
            temp //= 12

        temp = i
        while temp > 0:
            retSix += temp % 16
            temp //= 16

        if ret == retTwo and retTwo == retSix:
            print(i)
solution()