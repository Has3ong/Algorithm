def divisors(n):
    i = 2
    total = 1
    while i < n:
        if n % i == 0:
            total += i
        i += 1
    return total

ret = 0
for i in range(1, 10000):
    value = divisors(i)
    if i != value and divisors(value) == i:
        print(i, value)
        ret += i + value
print(ret // 2)
