import hashlib
def solution():
    string = str(input())
    encoded_string = string.encode()
    hexdigest = hashlib.sha512(encoded_string).hexdigest()
    print(hexdigest)
solution()
