def solution():
    String = str(input())
    A, B = String, String

    aCnt = 0
    nDelimiter = 0
    idx = 0
    while True:
        if not String: break

        nDelimiter = A.find('JOI')
        if nDelimiter >= 0:
            aCnt += 1
            idx += nDelimiter + 3
            A = A[idx:]
            idx = 0

        else: break

    bCnt = 0
    nDelimiter = 0
    idx = 0
    while True:
        if not String: break

        nDelimiter = B.find('IOI')
        if nDelimiter >= 0:
            bCnt += 1
            idx += nDelimiter + 2
            B = B[idx:]
            idx = 0

        else:
            break

    print(aCnt)
    print(bCnt)

solution()