from collections import deque

MAX = 100000
def bfs(N, K, dist):
    path = [0] * (MAX+1)
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            ret = []
            while x != N:
                ret.append(x)
                x = path[x]
            ret.append(N)
            ret.reverse()

            for i in ret:
                print(i, end=(' '))
            return

        if x-1 >= 0:
            if not dist[x - 1]:
                dist[x-1] = dist[x] + 1
                q.append(x-1)

                path[x-1] = x

        if x + 1 <= MAX:
            if not dist[x + 1]:
                dist[x+1] = dist[x] + 1
                q.append(x+1)

                path[x+1] = x

        if x*2 <= MAX:
            if not dist[x * 2] :
                dist[x*2] = dist[x] + 1
                q.append(x*2)

                path[x*2] = x

def solution():
    N, K = map(int, input().split(' '))
    dist = [0] * (MAX + 1)
    bfs(N, K, dist)

solution()