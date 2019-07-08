def solution():
    Check = [0] * 42
    for i in range(10):
        N = int(input())
        Check[N % 42] += 1

    cnt = 0
    for i in range(42):
        if Check[i]:
            cnt += 1

    print(cnt)

solution()