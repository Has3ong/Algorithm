
def solution():
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = list(map(int,input().split(' ')))
        if sum(arr) > 0:
            print('Right')
        elif sum(arr) < 0:
            print('Left')
        else:
            print('Equilibrium')
solution()