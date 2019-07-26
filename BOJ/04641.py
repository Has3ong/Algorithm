def solution():

    while 1:
        cnt = 0
        Check = [False] * 101
        arr = list(map(int, input().split(' ')))
        if -1 in arr:
            break

        for i in arr:
            Check[i] = True

        for i in arr:
            if i < 50 and i:
                if Check[i*2]:
                    cnt += 1
        print(cnt)

solution()