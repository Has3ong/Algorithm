def solution():
    Board = []
    count = 0
    flag = 1

    for i in range(8):
        Board.append(list(map(str, input())))

    for i in range(8):
        for j in range(8):
            if flag == 1:
                if Board[i][j] == 'F':
                    count += 1
                flag = (flag + 1) % 2
            else:
                flag = (flag + 1) % 2
        flag = (flag + 1) % 2

    print(count)
solution()