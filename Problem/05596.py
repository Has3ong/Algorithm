def solution():
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))

    print(max(sum(A), sum(B)))
solution()