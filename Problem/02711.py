
def solution():
    T = int(input())
    for i in range(T):
        A, B = map(str, input().split(' '))
        arr = []
        for j in range (len(B)):
            arr.append(B[j])

        string = ''
        for j in range(len(arr)):
            if j == int(A)-1:
                continue
            string += arr[j]
        print(string)
solution()