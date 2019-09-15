def solution():
    string = str(input())
    temp = ''
    ret = ''
    tag = False

    for i in range(len(string)):
        if string[i] == '<':
            if temp:
                for j in range(len(temp)):
                    ret += temp[len(temp) - j - 1]
                temp = ''
            tag = True
            ret += '<'

        elif string[i] == '>':
            tag = False
            ret += '>'

        elif string[i] == ' ':
            if tag:
                ret += string[i]
            else:
                if temp:
                    for j in range(len(temp)):
                        ret += temp[len(temp) - j - 1]
                    temp = ''
                ret += string[i]

        else:
            if tag:
                ret += string[i]
            else:
                temp += string[i]

    if temp:
        for j in range(len(temp)):
            ret += temp[len(temp) - j - 1]
        temp = ''
    print(ret)
solution()