
def solution():
    for i in range(101):
        Cube = i * i * i
        for j in range(2, i):
            A = j * j * j
            for k in range(j, i):
                B = k * k * k
                for l in range(k, i):
                    C = l * l * l

                    if Cube == (A + B + C):
                        print('Cube = %d, Triple = (%d,%d.%d)' %(i, j, k, l))


solution()