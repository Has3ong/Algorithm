def solution():
    N = int(input())
    for i in range(N):
        s = str(input())
        if s[len(s)//2-1] == s[len(s)//2]:
            print('Do-it')

        else:
            print('Do-it-Not')
solution()