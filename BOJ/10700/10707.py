def solution():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    P = int(input())

    A = P * A
    if P - C >= 0:
        B = B + (P - C) * D

    print(min(A, B))
solution()