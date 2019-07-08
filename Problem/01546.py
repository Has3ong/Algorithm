def solution():
    num = int(input())
    max = 0
    avg = 0
    inArr = list(map(float, input().split()))
    for i in range(num):
        if max < inArr[i]:
            max = inArr[i]

    for i in range(num):
        inArr[i] = inArr[i] / max * 100.0
        avg += inArr[i]

    print(round(avg / num, 2))
solution()