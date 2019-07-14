def solution():
    _max = 0
    person = 0
    for i in range(10):
        A, B = map(int, input().split(' '))
        person = person - A + B
    print(_max)
solution()