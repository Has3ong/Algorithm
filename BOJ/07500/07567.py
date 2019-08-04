def solution():
    String = str(input())

    Height = 10
    for i in range(1, len(String)):
        if String[i-1] == String[i]:
            Height += 5
        else:
            Height += 10
    print(Height)
solution()