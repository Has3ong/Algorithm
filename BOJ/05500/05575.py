def solution():
    for i in range(3):
        sHour, sMinute, sSecond, eHour, eMinute, eSecond = map(int, input().split(' '))

        if eSecond - sSecond < 0:
            eMinute -= 1
            eSecond = 60 + eSecond - sSecond
        else:
            eSecond = eSecond - sSecond

        if eMinute - sMinute < 0:
            eHour -= 1
            eMinute = 60 + eMinute - sMinute
        else:
            eMinute = eMinute - sMinute

        eHour = eHour - sHour

        print(eHour, eMinute, eSecond)


solution()