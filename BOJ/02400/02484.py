def solution():
    N = int(input())

    ret = 0
    for i in range(N):
        arr = [0] * 7
        A, B, C, D = map(int, input().split(' '))
        arr[A] += 1
        arr[B] += 1
        arr[C] += 1
        arr[D] += 1

        j = 0
        tmp = 0
        for i in range(len(arr)):
            if arr[i] == 4:
                ret = max(ret, (50000 + (i * 5000)))
                break

            if arr[i] == 3:
                ret = max(ret, (10000) + (i * 1000))
                break

            if arr[i] == 2:
                if arr[i] == 2 and tmp:
                    ret = max(ret, (2000 + (i * 500) + (j * 500)))
                    break
                j = i
                tmp = 1

            if tmp == 1 and i == 6:
                ret = max(ret, 1000 + (j * 100))
                break

            if tmp == 1:
                continue

            if arr[i] == 1 and not tmp:
                num = i
                ret = max(ret, (100 * i))
    print(ret)
solution()