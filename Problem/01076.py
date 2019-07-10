def solution():
    dic = {
        'black' : 0,
        'brown' : 1,
        'red' : 2,
        "orange" : 3,
        "yellow" : 4,
        "green" : 5,
        "blue" : 6,
        "violet" : 7,
        "grey" : 8,
        "white" : 9
    }
    A = str(input())
    B = str(input())
    C = str(input())

    ohm = (dic.get(A) * 10 + dic.get(B))
    for i in range(dic.get(C)):
        ohm *= 10
    print(ohm)
solution()