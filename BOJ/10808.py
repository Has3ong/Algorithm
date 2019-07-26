def solution():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ret = [0] * 26
    string = str(input())
    for i in range(len(string)):
        ret[alphabet.index(string[i])] += 1

    for i in ret:
        print(i, end=' ')
solution()