
def solution():
    T = int(input())
    for i in range(T):
        A = str(input())
        B = list(str(input()))
        string = ''
        for i in range(len(A)):
            if ord(A[i]) < 65:
                string += ' '
            else:
                string += B[ord(A[i]) - 65]
        print(string)
solution()