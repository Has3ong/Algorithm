def solution():
    while 1:
        flag = 1
        N = str(input())
        if N == '0':
            break

        for i in range(len(N)//2):
            if N[i] != N[len(N) - 1 - i]:
                print('no')
                flag = 0
                break
        if flag:
            print('yes')
solution()