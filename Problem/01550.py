
def solution():
    NUM = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    X = str(input())

    mul = 1
    ret = 0
    for i in range(len(X)):
        ret = ret + (NUM.index(X[len(X) - i - 1])) * mul
        mul *= 16
    print(ret)
solution()