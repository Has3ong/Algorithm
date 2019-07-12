import sys
from collections import deque

def dfs(Graph, start, visit, ret):
    ret.append(start)
    visit.append(start)
    for i in range(len(Graph)):
        if Graph[start][i] == 1 and i not in visit:
            dfs(Graph, i, visit, ret)


def bfs(Graph, start, visit, ret):
    dq = deque()
    dq.append(start)

    while len(dq) > 0:
        start = dq.popleft()
        if start not in visit:
            visit.append(start)
            ret.append(start)

        for i in range(len(Graph)):
            if Graph[start][i] == 1 and i not in visit:
                dq.append(i)


def solution():
    N, M, V = map(int,input().split(' '))
    Graph = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        Graph[x][y] = 1
        Graph[y][x] = 1

    retDFS = []
    retBFS = []
    visit = []
    dfs(Graph, V, visit, retDFS)
    visit = []
    bfs(Graph, V, visit, retBFS)

    res1 = ''
    res2 = ''
    for i in range(len(retDFS)):
        res1 += str(retDFS[i])
        res2 += str(retBFS[i])
        res1 += ' '
        res2 += ' '

    print(res1)
    print(res2)

solution()