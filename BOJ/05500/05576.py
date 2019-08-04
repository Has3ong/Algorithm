def solution():
    Wscore = []
    for i in range(10):
        Wscore.append(int(input()))
    Kscore = []
    for i in range(10):
        Kscore.append(int(input()))

    Wscore.sort()
    Kscore.sort()
    print(Wscore[7] + Wscore[8] + Wscore[9], Kscore[7] + Kscore[8] + Kscore[9])

solution()