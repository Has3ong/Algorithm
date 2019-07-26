A, B = map(int, input().split())

i = 0
result = (str(A//B)+".")
d = A%B
while i < 1000:
    d *= 10
    m = d//B
    result += str(m)
    d %= B
    if d == 0:
        break
    i += 1
print(result)