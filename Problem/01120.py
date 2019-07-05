def solution():
    A, B = map(str, input().split(' '))

    MIN = 101
    for i in range(0, len(B) - len(A) + 1):
        cnt = 0
        for j in range(0, len(A)):
            if A[j] != B[j+i]:
                cnt += 1
        MIN = min(MIN, cnt)
    print(MIN)

solution()