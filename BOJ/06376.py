print("n e")
print("- -----------")
print("0 1")
print("1 2")
print("2 2.5")

ret = 2.5
fact = 2
for i in range(3, 10):
    fact *= i
    ret += 1.0/fact
    print("%d %.9f" % (i, ret))