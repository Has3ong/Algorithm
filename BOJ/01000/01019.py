def myrange(start, end, step):
    r = start
    while(r > end):
        yield r
        r = int(r / step)

def solve(start, div, Count):
    for i in myrange(start, 0, 10):
        Count[i%10] += div

def solution():
    N = int(input())
    Count = [0] * 10
    start = 1
    div = 1

    while start <= N:
        while start % 10 != 0 and start <= N:
            solve(start, div, Count)
            start += 1

        if start > N:
            break

        while N % 10 != 9 and start <= N:
            solve(N, div, Count)
            N -= 1

        cnt = int((N / 10) - (start / 10) + 1)
        for i in range (10):
            Count[i] += cnt * div

        start = int(start / 10)
        N  = int(N / 10)
        div *= 10

    string = ""
    for i in range(10):
        string += str(int(Count[i]))
        if i < 9:
            string += " "
    print(string)
solution()