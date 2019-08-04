def solution():
    N = int(input())
    if N % 2 == 1:
        for i in range(N//2 + 2):
            if i == 0:
                string = ''
                for j in range(N):
                    string += '*'
                print(string)
                continue

            if i == 1:
                string = ''
                for j in range(N//2):
                    string += ' '
                string += '*'
                print(string)
                continue

            string = ''
            #i = 2
            for j in range(N//2 + 1 - i):
                string += ' '
            string += '*'
            cnt = 1 + (i - 2) * 2
            for j in range(cnt):
                string += ' '
            string += '*'
            print(string)

    else:
        print('I LOVE CBNU')
solution()