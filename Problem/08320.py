def solution():
    N = int(input())

    result = 0
    for i in range(1, N+1):
        for j in range(1, 2 * N):
            if j * j > i:
                break

            if i % j == 0:
                result += 1
    print(result)
solution()