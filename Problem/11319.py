def solution():
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    N = int(input())
    for j in range(N):
        A = str(input())

        vCnt = 0
        cCnt = 0
        for i in range(len(A)):
            if A[i] in vowels:
                vCnt += 1

            if A[i] in consonants:
                cCnt += 1

        print(cCnt, vCnt)
solution()