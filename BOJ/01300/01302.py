def solution():
    T = int(input())
    arr = [0] * 1001
    n_arr = []
    for i in range(T):
        name = str(input())
        if name in n_arr:
            arr[n_arr.index(name)] += 1
        else:
            n_arr.append(name)
            arr[n_arr.index(name)] += 1

    _max = 0

    for i in range(T):
        _max = max(_max, arr[i])

    ret = []
    for i in range(T):
        if arr[i] == _max:
            ret.append(n_arr[i])

    ret.sort()
    print(ret[0])

solution()