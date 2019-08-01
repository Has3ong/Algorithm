
def solution():
    N, M = map(int, input().split(' '))
    arr1 = list(map(int, input().split(' ')))
    arr2 = list(map(int, input().split(' ')))

    arr1.sort()
    arr2.sort()

    index1, index2 = 0, 0

    ret = ''
    while index1 + index2 < N + M :

        if index1 == N:
            print(arr2[index2], end=' ')
            index2 += 1

        elif index2 == M:
            print(arr1[index1], end=' ')
            index1 += 1

        else:
            if arr1[index1] > arr2[index2]:
                print(arr2[index2], end=' ')
                index2 += 1
            else:
                print(arr1[index1], end=' ')
                index1 += 1

solution()