def solution():
    test = 'CAMBRIDGE'

    string = str(input())
    for i in range(len(test)):
        string = string.replace(test[i], '')
    print(string)
solution()