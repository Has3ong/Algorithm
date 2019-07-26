def solution():
    result = []
    A, B = map(int, input().split(' '))
    C = 1
    for i in range(0, B):
        C = C * A
        C = C % 10
        if C in result:
            break
        result.append(C)

    C = result[B % len(result)-1]

    if C == 0:
        print(10)
    else :
        print(C)
T = int(input())

for i in range(T):
    solution()