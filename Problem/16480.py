def solution():
    R, r = map(int, input().split(' '))
    print( (R-r) * (R-r) - (r * r) )
solution()