def solution():
    binaryinit = ["0", "1", "10", "11", "100", "101", "110", "111"]
    binary = ["000", "001", "010", "011", "100", "101", "110", "111"]

    N = str(input())
    ret = ''
    for i in range(len(N)):
        if i == 0:
            ret += binaryinit[int(N[i])]
        else:
            ret += binary[int(N[i])]
    print(ret)

solution()