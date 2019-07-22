def solution():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    N = int(input())
    arr = list(str(input()))
    alphabet = []

    for i in range(N):
        alphabet.append(int(input()))

    Stack = []

    for i in range(len(arr)):
        if arr[i] in alpha:
            arr[i] = alphabet[alpha.index(arr[i])]

    for i in arr:
        if i == '+':
            a = Stack.pop()
            b = Stack.pop()
            Stack.append(a+b)
        elif i == '*':
            a = Stack.pop()
            b = Stack.pop()
            Stack.append(a * b)
        elif i == '-':
            b = Stack.pop()
            a = Stack.pop()
            Stack.append(a - b)
        elif i == '/':
            b = Stack.pop()
            a = Stack.pop()
            Stack.append(a / b)
        else:
            Stack.append(i)

    print('%0.2f' %Stack[0])
solution()