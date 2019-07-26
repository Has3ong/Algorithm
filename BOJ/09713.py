def solution():
    arr = [0]

    j = 1
    for i in range(1, 101):
        arr.append(arr[i-1] + j)
        j = j + 2
    N = int(input())

    for i in range(N):
        A = int(input())
        print(arr[A//2 + 1])

solution()