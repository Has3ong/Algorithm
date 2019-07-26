ans = 2

a = 1
b = 2
c = 0
while 1:
    if c > 4000000:
        break

    c = a + b
    a = b
    b = c

    if c % 2 == 0:
        ans += c

print(ans)