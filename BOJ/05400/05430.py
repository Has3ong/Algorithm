from collections import deque

def solution():
    T = int(input())
    for i in range(T):
        dq = deque()

        command = str(input())
        N = int(input())
        Array = str(input())

        ret = ''
        for i in range(1, len(Array)):
            if Array[i] == ',' or Array[i] == ']':
                dq.append(ret)
                ret = ''
            else:
                ret += Array[i]

        cnt = 0
        for j in range(len(command)):
            if command[j] == 'D':
                cnt += 1
        if cnt > N:
            print('error')
            continue
        elif cnt >= N:
            print('[]')
            continue

        flag = 1
        for j in range(len(command)):
            if command[j] == 'R':
                if flag:
                    flag = 0
                else:
                    flag = 1

            if command[j] == 'D':
                if len(dq):
                    if flag:
                        dq.popleft()
                    else:
                        dq.pop()
                else:
                    print('error')
                    break

        res = '['
        if flag:
            for i in range(len(dq)):
                if i == len(dq) - 1:
                    res += dq[i]
                    continue
                res += dq[i] + ','

        else:
            for i in range(len(dq)):
                if i == len(dq) - 1:
                    res += dq[len(dq) - i - 1]
                    continue
                res += dq[len(dq) - i - 1] + ','
        res += ']'
        print(res)


solution()