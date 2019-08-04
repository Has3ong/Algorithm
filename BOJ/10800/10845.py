import sys

class Queue:
    def __init__(self):
        self.data = []
        self.h = -1
    def push(self, v):
        self.h += 1
        self.data.insert(0, v)
    def pop(self):
        if self.h == -1:
            return -1
        else:
            self.h -= 1
            return(self.data.pop())
    def empty(self):
        if self.h == -1 :
            return 1
        else :
            return 0
    def front(self):
        if self.h == -1 :
            return -1
        else :
            return self.data[-1]
    def back(self):
        if self.h == -1:
            return -1
        else:
            return self.data[0]
    def size(self):
        return (self.h + 1)

def solution():
    N = int(input())
    S = Queue()
    for i in range(N):
        command = sys.stdin.readline()

        nDelimiter = 0
        nDelimiter = command.find('push')
        if nDelimiter >= 0:
            command = int(command[4:])
            S.push(command)
            continue

        nDelimiter = 0
        nDelimiter = command.find('front')
        if nDelimiter >= 0:
            print(S.front())
            continue

        nDelimiter = 0
        nDelimiter = command.find('size')
        if nDelimiter >= 0:
            print(S.size())
            continue

        nDelimiter = 0
        nDelimiter = command.find('pop')
        if nDelimiter >= 0:
            print(S.pop())
            continue

        nDelimiter = 0
        nDelimiter = command.find('empty')
        if nDelimiter >= 0:
            print(S.empty())
            continue
        nDelimiter = 0
        nDelimiter = command.find('back')
        if nDelimiter >= 0:
            print(S.back())
            continue

solution()