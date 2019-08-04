def solution():
    while 1:
        arr = list(map(int, input().split(' ')))
        arr.sort()

        a = arr[0]
        b = arr[1]
        c = arr[2]

        if a == 0 and b == 0 and c == 0:
            break
        if a * a + b * b == c * c:
            print('right')
        else:
            print('wrong')


solution()