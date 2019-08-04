def solution():
    N = int(input())
    operator = str(input())
    M = int(input())

    if operator == '*':
        print(N*M)
    else:
        print(N+M)
solution()