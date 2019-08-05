def solution():
    N, M = map(int, input().split(' '))

    matrix1 = []
    for i in range(N):
        matrix1.append(list(map(int, input().split(' '))))

    M, K = map(int, input().split(' '))
    matrix2 = []
    for j in range(M):
        matrix2.append(list(map(int, input().split(' '))))

    for i in range(N):
        for j in range(K):
            sum = 0
            for k in range(M):
                sum += matrix1[i][k] * matrix2[k][j]
            print(sum, end=' ')
        print()

solution()