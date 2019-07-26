
def solution():
    N = int(input())
    if N < 5:
        print('PREDAJA')
        return

    Check = [0] * 26
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(N):
        name = str(input())
        Check[Alphabet.index(name[0])] += 1

    ret = []
    for i in range(26):
        if Check[i] >= 5:
            ret.append(Alphabet[i])

    if not ret:
        print('PREDAJA')
    else:
        for i in ret:
            print(i, end='')

solution()