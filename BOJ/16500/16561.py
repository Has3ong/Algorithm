def solution():
    N = int(input())

    cnt = 0
    for i in range(3, N + 1, 3):
        for j in range(3, N + 1, 3):
            if i + j < N:
                cnt += 1

    print(cnt)


solution()