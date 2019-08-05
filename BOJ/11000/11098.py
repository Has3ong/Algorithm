def solution():
    T = int(input())

    for i in range(T):
        N = int(input())

        retName, retValue = '', 0

        for j in range(N):
            value, name = map(str, input().split(' '))

            if int(value) > int(retValue):
                retValue = value
                retName = name

        print(retName)

solution()