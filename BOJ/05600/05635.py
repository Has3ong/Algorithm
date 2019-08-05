def solution():
    T = int(input())

    arr = []
    for i in range(T):
        Name, Day, Month, Year = map(str, input().split(' '))
        arr.append([int(Year), int(Month), int(Day), Name])
    arr.sort()
    print(arr[-1][3])
    print(arr[0][3])
solution()