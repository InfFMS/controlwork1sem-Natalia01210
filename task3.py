def T(A, B):
    return bool((not A) or B)
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (T(x == z, ((not y) or w)) == (T(w, z) or T(x, y))) and ((T(w, z) or T(x, y))) == True:
                    print(x, y, z, w)
                    print()