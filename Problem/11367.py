def solution():
    T = int(input())
    for i in range(T):
        N, M = map(str, input().split(' '))

        if int(M) >= 97:
            print(N, 'A+')
            continue
        if int(M) >= 90:
            print(N, 'A')
            continue
        if int(M) >= 87:
            print(N, 'B+')
            continue
        if int(M) >= 80:
            print(N, 'B')
            continue
        if int(M) >= 77:
            print(N, 'C+')
            continue
        if int(M) >= 70:
            print(N, 'C')
            continue
        if int(M) >= 67:
            print(N, 'D+')
            continue
        if int(M) >= 60:
            print(N, 'D')
            continue
        if int(M) <= 59:
            print(N, 'F')
            continue
solution()