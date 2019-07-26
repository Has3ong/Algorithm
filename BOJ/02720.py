def solution():
    N = int(input())

    for i in range(N):
        ret = []
        A = int(input())
        ret.append(A // 25)
        A %= 25

        ret.append(A // 10)
        A %= 10

        ret.append(A // 5)
        A %= 5

        ret.append(A // 1)
        for j in ret:
            print(j, end=' ')

solution()