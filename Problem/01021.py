def left(Queue, step):
    step[0] += 1

    tmp = Queue.pop(0)
    Queue.append(tmp)

def right(Queue, step):
    step[0] += 1

    temp = [Queue.pop(-1)]
    temp.extend(Queue)
    return temp


def solution():
    step = [0]

    n, m = map(int, input().split())
    idx = list(map(int, input().split()))
    Queue = list(range(1, n + 1))

    while idx:

        if Queue[0] == idx[0]:
            Queue.pop(0)
            idx.pop(0)
        else:
            if Queue.index(idx[0]) <= len(Queue) // 2:
                while Queue[0] != idx[0]:
                    left(Queue, step)
            else:
                while Queue[0] != idx[0]:
                    Queue = right(Queue, step)

    print(step[0])

solution()