def solution():
    X, Y, W, H = map(int, input().split(' '))
    print(min(W-X, H-Y, X, Y))

solution()