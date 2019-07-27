
def solution():
    N, R, C = map(int,input().split(' '))

    for i in range(N):
        string = ''
        for j in range(N):
            if (i+j) % 2 != ((R-1) + (C-1)) % 2:
                string += '.'
            else:
                string += 'v'
        print(string)

solution()