
def function(X, N, end):
    next = 0
    num = (N - 1) // X

    if num == 0:
        end[0] = N
        return 1
    else:
        next = (N - 1) // num

    ret = (num + 1) * (next - X + 1)
    end[0] = next

    return ret

def solution():
    end = [1]
    N = int(input())
    ret = N

    while end[0] < N:
        print(end, ret, N)
        ret += function(end[0] + 1, N, end)

    print(ret)
solution()