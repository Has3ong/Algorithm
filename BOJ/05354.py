def solution():
    T = int(input())

    for i in range(T):
        N = int(input())
        if N == 1:
            print('#\n')
            continue

        string = ''
        for j in range(N):
            string += '#'
        print(string)

        for j in range(N-2):
            string = ''
            for k in range(N):
                if k == 0 or k == N-1:
                    string += '#'
                else:
                    string += 'J'
            print(string)

        string = ''
        for j in range(N):
            string += '#'
        print(string)
        print('')

solution()
