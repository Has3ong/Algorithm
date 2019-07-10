def solution():
    a = int(input())

    group_num = a
    num = 1
    while group_num > 0:
        group_num -= num
        num += 1

    total_num = (num-2)*(num-1)/2

    numerator = a - total_num
    denominator = num - numerator

    if num % 2 !=0:
        print("{0}/{1}".format(int(numerator),int(denominator)))
    else:
        print("{0}/{1}".format(int(denominator),int(numerator)))
solution()