
def solution():
    N = int(input())
    score = list(map(int, input().split(' ')))

    ret = 0
    cnt = 1

    for i in range(N):
        if score[i] == 1:
            ret += cnt
            cnt += 1
        else:
            cnt = 1
    print(ret)

solution()