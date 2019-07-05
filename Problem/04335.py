def solution():
    Check = [True] * 11
    while 1:
        T = int(input())
        if T == 0:
            return
        S = str(input())
        if S == 'too high':
            for i in range(T, 11):
                Check[i] = False
        elif S == 'too low':
            for i in range(0, T+1):
                Check[i] = False
        else:
            if Check[T]:
                print('Stan may be honest')
            else:
                print('Stan is dishonest')
            Check = [True] * 11

solution()