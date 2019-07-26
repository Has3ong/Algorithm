ans = []

for i in range(100, 1000):
    for j in range(100, 1000):
        flag = 1
        com = str(i * j)

        for k in range(len(com) // 2):
            if com[k] != com[len(com) - k - 1]:
                flag = 0
                break
        if flag:
            ans.append(int(com))
        else:
            continue
ans.sort()
print(ans)