A = 0
B = 0
for i in range(1, 101):
    A += i * i
    B += i

print((B * B) - A)