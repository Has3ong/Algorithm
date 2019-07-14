A = [0] * 10
B = [0] * 10
checkA = [0] * 10
checkB = [0] * 10
Use = [False] * 10

def dfs(pos, N, J, ret):
    checkA[pos] = A[J]
    checkB[pos] = B[J]

    tempA = 1
    tempB = 0
    for i in range(pos+1):
        tempA *= checkA[i]
        tempB += checkB[i]

    ret[0] = min(ret[0], abs(tempA-tempB))
    if pos == N:
        return

    for i in range(J, N):
        if not Use[i] :
            Use[i] = True
            dfs(pos + 1, N, i, ret)
            Use[i] = False

def solution():
    ret = [1000000001]
    N = int(input())
    for i in range(N):
        a, b = map(int, input().split(' '))
        A[i] = a
        B[i] = b

    for i in range(N):
        Use[i] = True
        dfs(0, N, i, ret)
        Use[i] = False

    print(ret[0])

solution()