def solution():
    N = str(input())
    T = int(input())
    arr = []
    n_arr = []
    mod = 100
    for i in range(T):
        name = str(input())
        n_arr.append(name)

        LOVE = [0, 0, 0, 0]

        for j in range(len(N)):
            if N[j] == 'L':
                LOVE[0] += 1
            elif N[j] == 'O':
                LOVE[1] += 1
            elif N[j] == 'V':
                LOVE[2] += 1
            elif N[j] == 'E':
                LOVE[3] += 1
            else:
                continue

        for j in range(len(name)):
            if name[j] == 'L':
                LOVE[0] += 1
            elif name[j] == 'O':
                LOVE[1] += 1
            elif name[j] == 'V':
                LOVE[2] += 1
            elif name[j] == 'E':
                LOVE[3] += 1
            else:
                continue
        value = 0
        value = ((LOVE[0] + LOVE[1]) * (LOVE[0] + LOVE[2]) * (LOVE[0] + LOVE[3]) * (LOVE[1] + LOVE[2]) * (LOVE[1] + LOVE[3]) * (LOVE[2] + LOVE[3])) % mod
        arr.append(value)

    _max = 0
    ret = []
    for i in range(T):
        _max = max(_max, arr[i])

    for i in range(T):
        if arr[i] == _max:
            ret.append(n_arr[i])
    ret.sort()
    print(ret[0])
solution()