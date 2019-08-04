def solution():
    T = int(input())
    for i in range(T):
        A, B = map(str, input().split(' '))

        if B == 'kg':
            print('%0.4f lb' %(float(A) * 2.2046))
        elif B == 'l':
            print('%0.4f g' %(float(A) * 0.2642))
        elif B == 'lb':
            print('%0.4f kg' %(float(A) * 0.4536))
        elif B == 'g':
            print('%0.4f l' %(float(A) * 3.7854))

solution()