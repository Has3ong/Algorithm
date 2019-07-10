def solution():
    N, A, B = map(int, input().split(' '))

    count = 0

    flag = 1

    while N != 1:
        count += 1
        N /= 2
        A = (A + 1) // 2
        B = (B + 1) // 2

        if A == B:
            print(count)
            flag = 0
            break
    if flag:
        print(-1)


solution()