def solution():
    A, B = map(str, input().split(' '))

    temp = 0
    mul = 1
    for i in range(len(A)):
        temp += int(A[len(A) - 1 - i]) * (mul)
        mul *= 2

    tempB = 0
    mul = 1
    for i in range(len(B)):
        tempB += int(B[len(B) - 1 - i]) * (mul)
        mul *= 2

    ret = ''
    res = temp + tempB

    if res == 0:
        print(0)
        return

    div = 2
    while res > 1:
        ret += str(res % div)
        res = res // div

    ret += '1'
    ret = ret[::-1]
    print(ret)


solution()
