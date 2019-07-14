def solution():
    check = [0] * 31
    for i in range(28):
        check[int(input())] += 1

    for i in range(1, 31):
        if not check[i]:
            print(i)
solution()