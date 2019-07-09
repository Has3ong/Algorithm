def Rev(String):
    ret = ''
    for i in range(len(String)):
        ret += String[len(String) - i - 1]
    return ret

def solution():
    X, Y = map(str, input().split(' '))
    ret = 0

    ret = int(Rev(str(int(Rev(X)) + int(Rev(Y)))))
    print(ret)
solution()
