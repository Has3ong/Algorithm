def solution():
    T = int(input())
    for i in range(T):
        A, B = map(int, input().split(' '))
        print('Case %d: %d' %(i+1, A+B))
solution()
