from collections import deque

MAX = 100000
def bfs(N, K, dist):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])

            return

        if x-1 >= 0:
            if not dist[x - 1]:
                dist[x-1] = dist[x] + 1
                q.append(x-1)

        if x + 1 <= MAX:
            if not dist[x + 1]:
                dist[x+1] = dist[x] + 1
                q.append(x+1)

        if x*2 <= MAX:
            dist[x*2] = dist[x]
            q.append(x*2)

def solution():
    N, K = map(int, input().split(' '))
    dist = [0] * (MAX + 1)
    bfs(N, K, dist)

solution()