
def solution():
    N = int(input())
    arrN = list(map(int, input().split(' ')))
    M = int(input())
    arrM = list(map(int, input().split(' ')))

    arrN.sort()

    for i in range(M):
        flag = 0

        left = 0
        right = len(arrN)

        while left < right:
            mid = (left + right) // 2

            if left == mid and arrM[i] != arrN[mid]:
                break

            if arrM[i] > arrN[mid]:
                left = mid
            elif arrM[i] < arrN[mid]:
                right = mid
            elif arrM[i] == arrN[mid]:
                flag = 1
                print(1)
                break


        if flag == 0:
            print(0)
solution()