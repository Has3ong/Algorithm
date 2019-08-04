def solution():
    N = int(input())
    arr = list(map(int, input().split(' ')))

    computer = [0] * 101
    cnt = 0
    for i in arr:
        if computer[i] == 0:
            computer[i] = 1
            continue
        else:
            cnt += 1
    print(cnt)
solution()