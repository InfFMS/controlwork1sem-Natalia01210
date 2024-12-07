def F(n):
    m = []
    for i in range(1, int(n ** 0.5) + 1, 1):
        if (n % i == 0):
            m.append(i)
            if (i != int(n ** 0.5)):
                m.append(n // i)
                m.sort(reverse = True)
    m.pop(0)
    m.pop(-1)
    if (len(m) < 5):
        return 0
    else:
        return m[4]
i=300000001
cnt = 0
while True:
    if (F(i) > 0 and cnt < 5):
        print(i)
        cnt+=1
    i+=1