def solution():
    A, B = map(str, input().split(' '))

    Atemp = 0
    Btemp = 0
    for i in range(len(A)):
        Atemp += int(A[i])
    for j in range(len(B)):
        Btemp += int(B[j])

    print(Atemp*Btemp)
solution()