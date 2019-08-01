
def solution():
    hour, minute, second = map(int, input().split(' '))
    time = int(input())

    second += time % 60
    time //= 60
    minute += time % 60
    time //= 60
    hour += time % 24

    if second >= 60:
        minute += 1
        second -= 60

    if minute >= 60:
        hour += 1
        minute -= 60

    if hour >= 24:
        hour -= 24

    print(hour, minute, second)
solution()