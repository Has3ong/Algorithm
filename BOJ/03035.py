def solution():
    x, y, r, c = map(int,input().split(' '))

    scanner = []
    for i in range(x):
        scanner.append(list(str(input())))

    for i in range(x):
        string = ''
        for j in range(y):
            for k in range(c):
                string += scanner[i][j]
        for l in range(r):
            print(string)
solution()