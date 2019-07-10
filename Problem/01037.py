def solution():
    N = int(input())
    yak = list(map(int, input().split()))
    print(min(yak) * max(yak))

solution()
