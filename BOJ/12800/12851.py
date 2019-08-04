from collections import deque

MAX = 100000
def bfs(N, K, dist):
    q = deque()
    q.append(N)
    ret, cnt = 0, 0
    while not cnt:
        s = len(q)
        while s:
            s -= 1
            x = q.popleft()
            if x == K:
                cnt += 1

            if x-1 >= 0:
                if not dist[x - 1] or dist[x - 1] == dist[x] + 1:
                    dist[x-1] = dist[x] + 1
                    q.append(x-1)

            if x + 1 <= MAX:
                if not dist[x + 1] or dist[x + 1] == dist[x] + 1:
                    dist[x+1] = dist[x] + 1
                    q.append(x+1)

            if x*2 <= MAX:
                if not dist[x * 2] or dist[x * 2] == dist[x] + 1:
                    dist[x*2] = dist[x] + 1
                    q.append(x*2)
        ret += 1
    print(ret - 1)
    print(cnt)

def solution():
    N, K = map(int, input().split(' '))
    dist = [0] * (MAX + 1)
    bfs(N, K, dist)

solution()