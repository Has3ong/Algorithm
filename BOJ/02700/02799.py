def solution():
    Blind = ['....', '*...', '**..', '***.', '****']

    Count = [0, 0, 0, 0, 0]

    N, M = map(int,input().split(' '))

    res = []
    for i in range((N * 5) + 1):
        res.append(list(str(input())))

    for i in range(N):
        for j in range(M):
            compare = ''
            compare += (
                res[(i * 5) + 1][(j * 5) + 1]
                +  res[(i * 5) + 2][(j * 5) + 1]
                +  res[(i * 5) + 3][(j * 5) + 1]
                +  res[(i * 5) + 4][(j * 5) + 1]
            )

            Count[Blind.index(compare)] += 1

    for i in Count:
        print(i, end=' ')
solution()