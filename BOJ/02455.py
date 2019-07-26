def solution():
    ret = 0
    _MAX = 0
    for i in range(4):
        a, b = map(int, input().split(' '))
        _MAX -= a
        _MAX += b
        ret = max(_MAX, ret)
    print(ret)
solution()
