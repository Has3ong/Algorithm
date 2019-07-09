import hashlib
def solution():
    string = str(input())
    encoded_string = string.encode()
    hexdigest = hashlib.sha384(encoded_string).hexdigest()
    print(hexdigest)
solution()
