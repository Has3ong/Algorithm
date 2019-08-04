def solution():
    Result = []
    N = int(input())
    Pattern = []
    length = 0
    for i in range(N):
        string = list(str(input()))
        Pattern.append(string)

    cnt = 1
    for i in range(len(string)):
        compare = ''
        cnt = 1
        flag = 0
        for j in range(N):
            if compare == '':
                compare = Pattern[j][i]
            elif compare == Pattern[j][i] :
                cnt += 1
            else :
                flag = 1
        if flag:
            Result.append('?')
        else :
            Result.append(Pattern[0][i])
    string = ''
    for i in Result:
        string += i
    print(string)

solution()