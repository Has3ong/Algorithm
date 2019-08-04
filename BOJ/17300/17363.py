def solution():
    N, M = map(int, input().split(' '))

    arr = []
    for i in range(N):
        arr.append(list(map(str, input())))
    print(arr)

    for i in range(M):
        string = ''
        for j in range(N):
            if arr[j][M - i - 1] == '-':
                string += '|'
            elif arr[j][M - i - 1] == '|':
                string += '-'
            elif arr[j][M - i - 1] == '/':
                string += '\\'
            elif arr[j][M - i - 1] == '\\':
                string += '/'
            elif arr[j][M - i - 1] == '^':
                string += '<'
            elif arr[j][M - i - 1] == '<':
                string += 'v'
            elif arr[j][M - i - 1] == 'v':
                string += '>'
            elif arr[j][M - i - 1] == '>':
                string += '^'
            else:
                string += arr[j][M - i - 1]
        print(string)

solution()