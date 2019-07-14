# PyPy3 제출
col = [0] * 15

def promising(i):
    for j in range(i):
        if col[j] == col[i] or abs(col[i] - col[j]) == (i-j):
            return False
    return True

def N_Queen(i, N, ret):
    if i == N:
        ret[0] += 1
    else:
        for j in range(N):
            col[i] = j
            if promising(i):
                N_Queen(i+1, N, ret)

def solution():
    N = int(input())
    ret = [0]
    N_Queen(0, N, ret)
    print(ret[0])
solution()