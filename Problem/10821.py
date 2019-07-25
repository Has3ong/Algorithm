def solution():
    N = str(input())

    arr = N.split(',')

    cnt = 0
    for i in arr:
        nDelimiter = i.find('.')
        if nDelimiter >= 0:
            continue
        else:
            cnt += 1
    print(cnt)
solution()