import hashlib
def solution():
    h = hashlib.new('sha')
    h.update(input().encode())
    print(h.hexdigest())
solution()
