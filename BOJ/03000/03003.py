def solution():
    Chess = list(map(int,input().split(' ')))
    print(1 - Chess[0], 1 - Chess[1], 2 - Chess[2], 2 - Chess[3], 2 - Chess[4], 8 - Chess[5])
solution()