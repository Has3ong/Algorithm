def solution():
    A = []
    B = []
    T = int(input())
    answer = [0] * T
    check = [0] * T
    B = input().split()
    for i in range(T):
        B[i] = int(B[i])

    for i in range(T):
        A.append(B[i])
    A.sort()

    for i in range(T):
        for j in range(T):
            if B[i] == A[j] and check[j] == 0:
                answer[i] = j
                check[j] = 1
                break

    string = ""
    for i in range (T):
        string += str(answer[i])
        if i < T-1:
            string += " "
    print(string)


solution()