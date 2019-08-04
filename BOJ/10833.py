def solution():
    T = int(input())
    ret = 0
    for i in range(T):
        Student, Apple = map(int,input().split(' '))

        ret += Apple % Student
    print(ret)
solution()