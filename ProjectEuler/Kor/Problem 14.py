MAX = 0
cntMAX = 0
for i in range(1, 1000000):
    cnt = 0
    
    temp = i
    N = i

    while 1:
        if N == 1:
            if cnt > cntMAX:
                MAX = temp
                cntMAX = cnt
            break

        if N % 2 == 0:
            N = N // 2
            cnt += 1

        else:
            N = 3 * N + 1
            cnt += 1

print(MAX, cntMAX)