def solution():
    while 1:
        A, B, C = map(str, input().split(' '))
        if A == '#':
            break

        if int(B) > 17 or int(C) >= 80:
            print(A, 'Senior')
        else:
            print(A, 'Junior')
solution()