def solution():
    arr =[]
    for i in range(9):
        arr.append(int(input()))

    temp = sum(arr) - 100

    A = 0
    B = 0
    for i in range(9):
        for j in range(9):
            if i != j and arr[i] + arr[j] == temp:
                A = i
                B = j

    for i in range(9):
        if i == A or i == B:
            continue
        print(arr[i])

solution()