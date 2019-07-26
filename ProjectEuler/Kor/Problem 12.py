def count_factors(num):
    loop = num ** 0.5
    if loop == int(loop):
        count = 1
    else:
        count = 0
    i = 1
    while i < loop:
        if num % i == 0:
            count += 2
        i += 1
    return count

i = 1
ret = 0
while True:
    ret = ret + i
    count = count_factors(ret)

    if count > 500:
        break
    i += 1

print(ret)