def solution():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))

    _max = 0
    cnt = 0

    for i in arr:
        if _max < i:
            _max = i
            cnt += 1

    print(cnt)

    _max = 0
    cnt = 0

    for i in range(N):
        if _max < arr[N - i - 1]:
            _max = arr[N - i - 1]
            cnt += 1
    print(cnt)

solution()