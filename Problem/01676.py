def solution():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if i % 5 == 0:
            num = i
            while 1:
                if num % 5 == 0:
                    cnt += 1
                    num //= 5
                else:
                    break
    print(cnt)
solution()