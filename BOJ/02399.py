def solution():
    N = int(input())
    arr = list(map(int, input().split(' ')))
    arr.sort()

    ret = 0
    temp = arr[0]
    for i in range(1, N):
        ret += arr[i] * i - temp
        temp += arr[i]
    print(ret * 2)

solution()