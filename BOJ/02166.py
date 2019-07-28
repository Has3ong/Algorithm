def ccw(x1, x2, x3):
    size = x1[0] * x2[1] + x2[0] * x3[1] + x3[0] * x1[1]
    size -= x1[0] * x3[1] + x2[0] * x1[1] + x3[0] * x2[1]
    return size

def solution():
    N = int(input())

    arr = []
    for i in range(N):
        x, y = map(int, input().split(' '))
        arr.append([x, y])

    ret = 0

    for i in range(1, N-1):
        ret += ccw(arr[0], arr[i], arr[i+1])
    print('%0.1f' %abs(ret/2))
solution()