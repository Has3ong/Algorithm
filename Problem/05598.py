def solution():
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Caesar = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

    code = str(input())
    ret = ''
    for i in range(len(code)):
        ret += Alphabet[Caesar.index(code[i])]
    print(ret)
solution()
