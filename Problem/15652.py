A = [0] * 8
def dfs(N, M, K, J):
    if K == M:
        string = ''
        for i in range(M):
            string += str(A[i] + 1)
            string += ' '
        print(string)
        return

    for i in range(J, N):
        A[K] = i
        dfs(N, M , K+1, i)

def solution():
    N, M = map(int, input().split(' '))
    if M == 1:
        for i in range(1, N+1):
            print(i)
    else:
        dfs(N, M, 0, 0)

solution()