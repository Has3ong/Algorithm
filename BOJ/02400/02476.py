def solution():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        val = 0
        if a == b == c:
            val = 10000 + a * 1000
        elif a == b or a == c:
            val = 1000 + a * 100
        elif b == c:
            val = 1000 + b * 100
        else:
            val = max([a, b, c]) * 100
        ans = max(val, ans)
    print(ans)

solution()