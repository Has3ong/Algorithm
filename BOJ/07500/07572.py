def solution():
    Alphabet = 'ABCDEFGHIJKL'
    year = int(input())

    JI = (8 + year % 12) % 12
    KAN = (5 + year % 10) % 10

    string = str(Alphabet[JI]) + str((KAN+1) % 10)
    print(string)
solution()