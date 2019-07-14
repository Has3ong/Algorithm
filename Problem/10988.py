
def solution():
    N = str(input())
    cnt = len(N) // 2
    length = len(N)

    for i in range(cnt):
        if N[i] != N[length - i - 1]:
            print(0)
            return
    print(1)
solution()