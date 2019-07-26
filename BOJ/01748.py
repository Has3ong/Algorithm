def solution():
    N = int(input())

    mod = 10
    mul = 9
    cnt = 1
    sum = 0
    while mod <= N:
        sum += (mul * cnt)
        mul *= 10
        mod *= 10
        cnt += 1

    sum += (N - (mod // 10) + 1) * cnt
    print(sum)
    
solution()