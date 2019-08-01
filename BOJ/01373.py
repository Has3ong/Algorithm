def solution():
    binary = ['000', '100', '010', '110', '001', '101', '011', '111']
    S = str(input())

    bin = ''
    for i in range(len(S)):
        bin += S[len(S) - i - 1]

    ret = ''
    for i in range(0, len(bin), 3):
        res = bin[i:i+3]
        if len(res) != 3:
            while len(res) != 3:
                res += '0'

        ret += str(binary.index(res))

    output = ''
    for i in range(len(ret)):
        output += ret[len(ret) - 1 - i]
    print(output)
solution()