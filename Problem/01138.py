
def solution():
    N = int(input())
    arr = list(map(int, input().split(' ')))

    line = []

    for i in range(len(arr)-1, -1, -1):
        line.insert(arr[i], i+1)

    for i in line:
        print(i, end=' ')

solution()