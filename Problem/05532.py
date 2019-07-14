def solution():
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    tempA = 0
    if A % C != 0:
        tempA += A // C + 1
    else:
        tempA += A // C
    tempB = 0
    if B % D != 0:
        tempB += B // D + 1
    else:
        tempB += B // D

    print(L - max(tempA, tempB))

solution()