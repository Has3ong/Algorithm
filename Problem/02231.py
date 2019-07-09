def solution():
    N = int(input())

    res = 10000000

    for i in range(1, res):
        num = i
        temp = 0
        temp += num
        while 1:
            if num < 100:
                temp = temp + num // 10
                temp = temp + num % 10
                break
            temp = temp + num % 10
            num = num // 10

        if N == temp:
            res = min(res, i)

    if res == 10000000:
        print(0)
    else:
        print(res)
solution()