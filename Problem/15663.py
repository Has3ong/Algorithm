A = [0] * 8
Use = [False] * 8


def dfs(N, M, K, Number):
    if K == M:
        string = ''
        for i in range(M):
            string += str(A[i])
            string += ' '
        print(string)
        return

    Check = [False] * 10001
    for i in range(N):
        if not Check[Number[i]] and not Use[i]:
            A[K] = Number[i]
            Use[i] = True
            Check[Number[i]] = True
            dfs(N, M, K + 1, Number)
            Use[i] = False


def solution():
    N, M = map(int, input().split(' '))
    Number = list(map(int, input().split(' ')))
    Number.sort()

    if M == 1:
        Check = [False] * 10001
        for i in Number:
            if not Check[i]:
                Check[i] = True
                print(i)
    else:
        dfs(N, M, 0, Number)


solution()