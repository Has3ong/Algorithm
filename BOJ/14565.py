def Inverse(N, A):
    if A >= 0:
        return A % N
    else:
        return (A + ((-1 * A) // N + 1) * N) % N

def solution():
    N, M = map(int, input().split(' '))

    R1 = N
    R2 = M
    T1 = 0
    T2 = 1

    while R2 > 0:
        Q = R1 // R2
        R = R1 - (Q * R2)
        T = T1 - (Q * T2)

        R1 = R2
        R2 = R
        T1 = T2
        T2 = T

    if R1 == 1:
        print(N-M, Inverse(N, T1))
    else:
        print(N-M, -1)

solution()