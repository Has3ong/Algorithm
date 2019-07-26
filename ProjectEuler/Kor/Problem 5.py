def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

ans = 0
SUM = 1
for i in range(1, 20):
    ans = lcm(i, SUM)
    SUM = ans
    print(ans)