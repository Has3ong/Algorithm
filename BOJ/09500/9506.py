def solution():
    while True:
        N = int(input())
        if N == -1:
            break

        ret = []
        for i in range(1, N):
            if N % i == 0:
                ret.append(i)

        String = str(N) + ' = '
        if sum(ret) == N:
            for i in range(len(ret)):
                if i != len(ret) - 1:
                    String += str(ret[i]) + ' + '
                else: String += str(ret[i])
            print(String)

        else:
            print("%d is NOT perfect." %N)
solution()