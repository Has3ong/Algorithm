def solution():
    N = int(input())
    A = 1
    temp = 1
    for i in range(N):
        temp *= 2

    A = A + temp
    print(A*A)
solution()