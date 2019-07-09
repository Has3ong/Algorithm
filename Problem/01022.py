def sol(dx, dy):
    if dx >= 0 and -1 * dx <= dy and dy <= dx :
        return (dx * 2 + 1) * (dx * 2 + 1) - (dx - dy)
    elif dx < 0 and dx <= dy and dy <= abs(dx) :
        return (abs(dx) * 2) * (abs(dx) * 2) - (abs(dx) -1) - dy
    elif dy > dx and dy > -1 * dx :
        return ((dy - 1) * 2 + 1) * ((dy - 1) * 2 + 1) + (dy - dx)
    else:
        return (abs(dy) * 2) * (abs(dy) * 2) + (dx - dy + 1)

def solution():
    R1, C1, R2, C2 = map(int, input().split(' '))

    length1 = str(sol(R1, C1))
    length2 = str(sol(R2, C2))
    length3 = str(sol(R1, C2))
    length4 = str(sol(R2, C1))

    length = -1
    length = max(len(length1), len(length2), len(length3), len(length4))

    for i in range (R1, R2+1):
        string = ""
        for j in range(C1, C2+1):
            l = len(str(sol(i, j)))
            for k in range(l, length):
                string += " "
            string += str(sol(i, j))
            string += " "
        print(string)
solution()