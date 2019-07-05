def solution():
    coin = [500, 100, 50, 10, 5, 1]
    N = int(input())

    K = 1000
    K = K - N

    cnt = 0
    for i in coin:
        cnt += K // i
        K = K % i
    print(cnt)
solution()