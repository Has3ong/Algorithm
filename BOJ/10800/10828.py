import sys
class Stack:
    def __init__(self):
        self.data = []
        self.h = -1
    def push(self, v):
        self.h += 1
        self.data.append(v)
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
    def top(self):
        if self.h == -1 :
            return -1
        else :
            return self.data[self.h]
    def size(self):
        return (self.h + 1)

def solution():
    N = int(input())
    S = Stack()
    for i in range(N):
        command = sys.stdin.readline()

        nDelimiter = 0
        nDelimiter = command.find('push')
        if nDelimiter >= 0:
            command = int(command[4:])
            S.push(command)
            continue

        nDelimiter = 0
        nDelimiter = command.find('top')
        if nDelimiter >= 0:
            print(S.top())
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

solution()