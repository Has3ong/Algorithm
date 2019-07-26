def solution():
    T = int(input())
    for i in range(T):
        arr = list(map(str, input().split(' ')))
        num = 0
        for j in range(len(arr)):
            if j == 0:
               num = float(arr[j])
            elif arr[j] == '@':
                num *= 3
            elif arr[j] == '%':
                num += 5
            elif arr[j] == '#':
                num -= 7
        print('%0.2f' %num)

solution()
