ans = 0
Used = [False] * 101
def dfs(position, count, ret, Card, N, M):
    global ans
    ret += Card[position]

    if count == 3:
        if ret <= M:
            ans = max(ans, ret)
        return

    if ret >= M:
        return

    for i in range(N):
        if not Used[i]:
            Used[i] = True
            dfs(i, count + 1, ret, Card, N, M)
            Used[i] = False


def solution():
    N, M = map(int, input().split(' '))
    Card = list(map(int,input().split(' ')))

    Card.sort()
    cnt = 0
    ret = 0
    for i in range(N):
        if not Used[i]:
            Used[i] = True
            dfs(i, cnt+1, ret, Card, N, M)
            Used[i] = False
    print(ans)

solution()