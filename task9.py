def F(e):
    m = []
    for i in range(1, int(e ** 0.5) + 1):
        if (e % i == 0):
            m.append(i)
            if (i != int(e ** 0.5)):
                m.append(e // i)
    return m
print(len(F(2097152)))