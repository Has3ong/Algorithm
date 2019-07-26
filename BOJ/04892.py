def solution():
    i = 1
    while 1:
        A = int(input())
        if A == 0:
            break
        A3 = 0
        A2 = A * 3
        if A2 % 2 == 1:
            A3 = (A2 + 1) //2
        else:
            A3 = A2 // 2

        A4 = A3 * 3
        A5 = A4 // 9

        if A2 % 2 == 1:
            print("%d. odd %d" %(i, A5))

        else:
            print("%d. even %d" % (i, A5))
        i += 1
solution()