#174457, 174506
m = []
for i in range(174457, 174506):
    m.append([])
    A = i
    for j in range(2, i):
        if(A % j == 0):
            m[i - 174457].append(j)

    if(len(m[i - 174457]) == 2):
        print(i)
        print(m[i - 174457][0])
        print(m[i - 174457][1])
        print()


