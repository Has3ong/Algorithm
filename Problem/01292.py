def solution():
    A, B = map(int, input().split(' '))

    arr = []
    temp = 0
    cnt = 1
    for i in range(10):
        if temp == cnt:
            temp = 0
            cnt += 1

        arr.append(cnt)
        temp += 1

    ret = 0
    for i in range(A - 1, B):
        ret += arr[i]
    print(ret)
solution()