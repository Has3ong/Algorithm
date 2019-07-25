
def solution():
    A, B = map(int, input().split(' '))
    C = int(input())

    B = B + C
    A = A + (B // 60)

    B %= 60
    A %= 24

    print(A, B)
solution()