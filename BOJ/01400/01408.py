def solution():
    Hour, Minute, Second = map(int, input().split(':'))
    EndHour, EndMinute, EndSecond = map(int, input().split(':'))


    Time = 3600 * Hour + 60 * Minute + Second
    EndTime = 3600 * EndHour + 60 * EndMinute + EndSecond

    left = EndTime - Time

    if left < 0:
        left += 86400

    Hour = left // 3600
    left %= 3600
    Minute = left // 60
    Second = left % 60
    print("%02d:%02d:%02d" %(Hour, Minute, Second))
solution()