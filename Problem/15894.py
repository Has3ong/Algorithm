def solution():
    N = int(input())

    cntBox = (N * (N+1)) // 2
    hide = ((N-1) * (N)) * 2

    print(cntBox * 4 - hide)
solution()