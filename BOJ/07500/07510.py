def solution():
    N = int(input())
    for i in range(1, N+1):
        arr = list(map(int,input().split(' ')))
        arr.sort()
        print('Scenario #%d:' %i)
        if arr[2] * arr[2] == arr[0] * arr[0] + arr[1] * arr[1]:
            print('yes\n')
        else:
            print('no\n')
solution()