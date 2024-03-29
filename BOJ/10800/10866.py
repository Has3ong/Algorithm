import sys
from collections import deque
class Deck:
    def __init__(self):
        self.data = deque()

    def push_back(self, value):
        self.data.append(value)
    def push_front(self, value):
        self.data.appendleft(value)
    def front(self):
        if self.data:
            return self.data[0]
        else:
            return -1
    def size(self):
        return len(self.data)
    def empty(self):
        if self.data:
            return 0
        else:
            return 1
    def back(self):
        if self.data:
            return self.data[-1]
        else:
            return -1
    def pop_front(self):
        if self.data:
            return self.data.popleft()
        else:
            return -1
    def pop_back(self):
        if self.data:
            return self.data.pop()
        else:
            return -1

def solution():
    N = int(input())
    S = Deck()
    for i in range(N):

        command = sys.stdin.readline()
        nDelimiter = 0
        nDelimiter = command.find('push_back')
        if nDelimiter >= 0:
            command = int(command[9:])
            S.push_back(command)
            continue

        nDelimiter = 0
        nDelimiter = command.find('push_front')
        if nDelimiter >= 0:
            command = int(command[10:])
            S.push_front(command)
            continue

        nDelimiter = 0
        nDelimiter = command.find('pop_front')
        if nDelimiter >= 0:
            print(S.pop_front())
            continue

        nDelimiter = 0
        nDelimiter = command.find('pop_back')
        if nDelimiter >= 0:
            print(S.pop_back())
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

solution()