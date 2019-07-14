import sys
def solution():
    N = int(input())
    X = list(map(int, sys.stdin.readline().split()))
    arr = [0] * 102
    for i in range(1, N + 1):
        arr[i - 1] = i

    for i in range(N):
        idx = i
        if not X[i]:
            continue
        else:
            for j in range(X[i]):
                temp = arr[idx]
                arr[idx] = arr[idx + j - X[i]]
                arr[idx + j - X[i]] = temp

    string = ''
    for i in range(N):
        string += str(arr[i])
        string += ' '
    print(string)
solution()