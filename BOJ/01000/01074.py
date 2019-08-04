def Z(N, R, C, size):
    if N == 0 :
        return 1

    if R < size[N-1]:
        if C < size[N-1]:
            return Z(N-1, R, C, size)
        else:
            return size[N-1] * size[N-1] + Z(N-1, R, C - size[N-1] , size)
    else:
        if C < size[N-1]:
            return size[N-1] * size[N-1] * 2 + Z(N-1, R - size[N-1], C, size)
        else:
            return size[N-1] * size[N-1] * 3 + Z(N-1, R - size[N-1], C - size[N-1], size)

def solution():
    N, R, C = map(int,input().split(' '))
    size = [1]
    for i in range(1, 16):
        size.append(size[i-1] * 2)

    print(Z(N, R, C, size) - 1)

solution()