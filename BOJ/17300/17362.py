def solution():
    n = int(input())

    if (n % 8 >= 1 and n % 8 <= 5):
        print(n%8)
    elif (n % 8 == 6):
        print(4)
    elif (n % 8 == 7):
        print(3)
    elif (n % 8 == 0):
        print(2)

solution()