ans = 0
for i in range(0, 1001, 3):

    ans += i

for i in range(0, 1000, 5):

    ans += i

for i in range(0, 1000, 15):
    ans -= i

print(ans)