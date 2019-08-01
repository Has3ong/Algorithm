def solution():
    T = int(input())

    for i in range(T):
        arr = list(map(int, input().split(' ')))
        ret = []
        total = 0
        for j in arr:
            if j % 2 == 0:
                ret.append(j)
                total += j

        print(total, min(ret))

solution()