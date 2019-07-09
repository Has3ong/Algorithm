one = []
zero = []

one.append(0)
one.append(1)
zero.append(1)
zero.append(0)

for i in range(2, 41):
    one.append(one[i - 1] + one[i - 2])
    zero.append(zero[i - 1] + zero[i - 2])


def solution():
    N = int(input())
    print(zero[N], one[N])


T = int(input())

for i in range(T):
    solution()