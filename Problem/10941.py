import base64

def solution():
    N = str(input())
    b = N.encode("UTF-8")
    print(str(base64.b16encode(b))[2:-1])

solution()