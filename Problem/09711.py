import sys

def solution():
    T = int(input())
    arr = [0, 1]
    for i in range(2, 10001):
        arr.append(arr[i-1] + arr[i-2])

    for i in range(T):
        p, q = map(int, sys.stdin.readline().split())
        print('Case #%d: %d' %(i+1, arr[p] % q))
solution()