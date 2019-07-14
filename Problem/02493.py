def solution():
    T = int(input())
    arr = list(map(int, input().split(' ')))
    Stack = []

    ret = []
    for i in range(T):

        while Stack:
            if Stack[-1][1] > arr[i]:
                ret.append(Stack[-1][0] + 1)
                break
            Stack.pop()

        if not Stack:
            ret.append(0)

        Stack.append([i, arr[i]])

    for i in range(T):
        print(ret[i], end=' ')


solution()