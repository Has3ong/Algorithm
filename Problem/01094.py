def solution():
    X = int(input())

    SUM = 0
    cnt = 0
    BAR = 64
    while 1:
        if SUM == X:
            print(cnt)
            return

        if SUM + BAR <= X:
            SUM += BAR
            BAR = BAR // 2
            cnt += 1
        else:
            BAR = BAR // 2

    print(cnt)
solution()