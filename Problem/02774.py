def solution():
    N = int(input())

    for i in range(N):
        arr = [0] * 10
        number = int(input())

        while number:
            arr[number % 10] += 1
            number //= 10

        ret = 0
        for j in arr:
            if j:
                ret += 1
        print(ret)


solution()