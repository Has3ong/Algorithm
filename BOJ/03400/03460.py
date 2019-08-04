def solution():
    T = int(input())
    for i in range (T):
        N = int(input())
        temp = N
        arr = []
        while 1:
            if temp <= 1:
                arr.append(1)
                break
            arr.append(temp % 2)
            temp //= 2

        ret = ''
        for i in range(len(arr)):
            if arr[i]:
                ret += str(i)
                ret += ' '
        print(ret)
solution()