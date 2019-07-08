def solution():
    T = int(input())
    while 1:
        N = int(input())
        if N == 0:
            break

        if N % T == 0:
            string = ''
            string += str(N)
            string += ' is a multiple of '
            string += str(T)
            string += '.'
            print(string)
        else:
            string = ''
            string += str(N)
            string += ' is NOT a multiple of '
            string += str(T)
            string += '.'
            print(string)

solution()