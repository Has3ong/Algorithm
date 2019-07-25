
def solution():
    score = []
    idx = []
    for i in range(8):
        A = int(input())
        if A == 0:
            idx.append(A)
            score.append(A)
            continue
        idx.append(A)
        score.append(A)

    score.sort(reverse=True)
    score.pop()
    score.pop()
    score.pop()

    print(sum(score))
    res = []
    for i in score:
        res.append(idx.index(i) + 1)
    res.sort()

    for i in res:
        print(i, end=' ')

solution()