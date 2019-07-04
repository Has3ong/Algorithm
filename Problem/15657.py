A = [0] * 8

def dfs(N, M, K, Number, J):
    if K == M:
        string = ''
        for i in range(M):
            string += str(A[i])
            string += ' '
        print(string)
        return

    for i in range(J, N):
        A[K] = Number[i]
        dfs(N, M, K + 1, Number, i)

def solution():
    N, M = map(int, input().split(' '))
    Number = list(map(int, input().split(' ')))
    Number.sort()
    if M == 1:
        for i in Number:
            print(i)
    else:
        dfs(N, M, 0, Number, 0)

solution()