
def dfs(i, cnt, pos, ret, N, K):
    temp = 0
    for i in range(0, pos[0]):
        temp += ret[i]

    if temp == N:
        if cnt[0] == K:
            res = ''
            for i in range(1, pos[0]):
                if i < pos[0] - 1:
                    res += str(ret[i])
                    res += '+'
                else:
                    res += str(ret[i])
            print(res)

        ret = [0] * 13
        cnt[0] += 1
        return

    elif temp >= N:
        return

    if pos[0] > N:
        return

    for i in range(1, 4):
        ret[pos[0]] = i
        pos[0] += 1
        dfs(i, cnt, pos, ret, N, K)
        pos[0] -= 1

def solution():
    N, K = map(int, input().split(' '))

    dp = [0, 1, 2, 4]
    for j in range(4, 13):
        dp.insert(j, dp[j - 1] + dp[j - 2] + dp[j - 3])

    if K > dp[N]:
        print(-1)
        return

    cnt = [1]
    ret = [0] * 13
    pos = [0]
    for i in range(1, 4):
        ret[1] = i
        pos[0] += 1
        dfs(i, cnt, pos, ret, N, K)
solution()