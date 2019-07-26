def solution():
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if i == 0 or j == 0 or k == 0:
                    continue

                if i + j + k == 1000:
                    if i * i + j * j == k * k:
                        print(i * j * k)
                        return


solution()