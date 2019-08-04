def solution():
    N = int(input())

    repeat = (N - 1) // 14
    tururu = 2 + repeat
    say = (N - 1) % 14

    if say == 0 or say == 12:
        print("baby")
    elif say == 1 or say == 13:
        print("sukhwan")
    elif say == 4:
        print("very")
    elif say == 5:
        print("cute")
    elif say == 8:
        print("in")
    elif say == 9:
        print("bed")
    else:
        tururu -= say % 2

        if tururu >= 5:
            print('tu+ru*%d'%tururu)
        else:
            string = 'tu'
            for i in range(tururu):
                string += 'ru'
            print(string)
solution()