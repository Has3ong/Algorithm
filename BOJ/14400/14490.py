def gcd(a, b):
    while b is not 0:
        d = a % b
        a = b
        b = d
    return a

def solution():
    N = str(input())
    length = N.find(':')

    A = int(N[0:length])
    B = int(N[length+1:])

    if A > B:
        d = gcd(A, B)
    else :
        d = gcd(B, A)

    string = ''
    string += str(A // d) + ':' + str(B // d)
    print(string)
solution()