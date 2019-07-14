def solution():
    N = int(input())
    for i in range(N):
        arr =[]
        arr = list(map(int, input().split(' ')))
        arr.sort()
        if arr[3] - arr[1] >= 4:
            print('KIN')
            continue
        else:
            print(sum(arr[1:4]))
solution()