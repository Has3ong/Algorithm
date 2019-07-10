
def solution():
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    N = int(input())

    cnt = [0] * 53
    secret = list(map(int,input().split(' ')))
    string = str(input())

    for i in secret:
        cnt[i] += 1

    for j in range(len(string)):
        index = Alphabet.find(string[j]) + 1
        cnt[index] -= 1

    for k in cnt:
        if not k == 0:
            print('n')
            return
    print('y')

solution()