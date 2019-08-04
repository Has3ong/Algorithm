def hanoi(n, _from, _to):
    if n != 0:
        hanoi(n-1, _from, 6 - _from - _to)
        print(_from, _to)
        hanoi(n-1, 6 - _from - _to, _to)

def solution():
    N = int(input())

    mul = 1
    for i in range(N):
        mul *= 2
    print(mul - 1)

    hanoi(N, 1, 3)

solution()