def solution():
    N = int(input())
    rope =[]
    for i in range(N):
        rope.append(int(input()))
    rope.sort()

    res = 0
    for i in range(N):
        res = max(res, rope[i] * (N-i))
    print(res)
solution()