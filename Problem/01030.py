def isBlack(i, N, K):
    return not((i < (N - K) / 2) or ((N - 1 - i) < (N - K) / 2))

def isRange(r1, r2, c1, c2, R1, R2, C1, C2):
    if r1 > R2 or r2 < R1:
        return 0
    if c1 > C2 or c2 < C1:
        return 0
    return 1

def POW(x, y):
    val = 1
    while y :
        y -= 1
        val *= x
    return val

def recursion(x, y, t, c, s, N, K, R1, R2, C1, C2, res):
    P = POW(N, s - t)
    if not isRange(x * P, x * P + P - 1, y * P, y * P + P - 1, R1, R2, C1, C2):
        return
    if t == s:
        res[x-R1][y-C1] = c
        return

    for i in range(N):
        for j in range(N):
            nc = 0
            if c == 1:
                nc = 1
            else:
                nc = int(isBlack(i, N, K) and isBlack(j, N, K))
            recursion(x*N+i, y*N+j, t+1, nc, s, N, K, R1, R2, C1, C2, res)

def solution():
    result = [[None] * 101 for i in range(101)]

    s, N, K, R1, R2, C1, C2 = map(int, input().split(' '))

    recursion(0,0,0,0,s,N,K,R1,R2,C1,C2, result)

    for i in range(R2 - R1 + 1):
        string = ''
        for j in range(C2 - C1 + 1):
            string += str(result[i][j])
        print(string)

solution()