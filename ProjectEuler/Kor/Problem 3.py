ans = 600851475143

a = 2
while 1:
    if ans % a == 0:
        print(a)
        while 1:
            ans = ans // a
            if ans % a != 0:
                break
    a += 1
