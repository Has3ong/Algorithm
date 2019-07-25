def solution():
    arr = [1]
    for i in range(30):
        arr.append(arr[-1] * 2)

    N = int(input())
    if N in arr:
        print(1)
    else:
        print(0)


solution()