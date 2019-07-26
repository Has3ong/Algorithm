def solution():
    check = ['000', '001', '010', '011', '100', '101', '110', '111']
    binary = ''
    s = str(input())

    if len(s) % 3 == 1:
        binary = '00' + s
    elif len(s) % 3 == 2:
        binary = '0' + s
    else:
        binary += s

    length = len(binary) // 3

    ret = ''
    for i in range(length):
        ret += str(check.index(binary[i * 3 : i * 3 + 3]))
    print(ret)
solution()