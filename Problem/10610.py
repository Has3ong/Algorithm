
def solution():
    arr = []
    N = str(input())

    res = 0
    for i in range(len(N)):
        res += int(N[i])

    if res % 3 != 0:
        print(-1)
        return

    for i in range(len(N)):
        arr.append(N[i])

    arr.sort(reverse=True)

    if '0' not in arr:
        print(-1)
        return

    string = ''
    for i in arr:
        string += i
    print(string)

solution()