
ret = 1
for i in range(1, 100):
    ret *= i

result = 0
while ret > 10:
    result += ret%10
    ret //= 10
print(result + ret)