def solution():
    mo = ['a','e','i','o','u','A','E','I','O','U']
    while 1:
        string = str(input())
        if string == '#':
            return

        cnt = 0
        for i in range(len(string)):
            if string[i] in mo:
                cnt += 1

        print(cnt)

solution()