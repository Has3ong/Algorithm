def solution():
    N = int(input())
    for i in range(N):
        S = list(map(str, input().split(' ')))

        ret = ''
        for i in range(2, len(S)):
            ret += S[i] +' '
        ret += S[0] + ' ' + S[1]
        print(ret)
solution()