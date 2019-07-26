import sys
def solution():
    N, M = map(int, input().split(' '))
    d = set()
    for i in range(N):
        d.add(sys.stdin.readline())

    ret = []
    for j in range(M):
        temp = sys.stdin.readline()
        if temp in d:
            ret.append(temp)

    ret.sort()
    print(len(ret))
    for i in ret:
        print(i[:-2])

solution()
