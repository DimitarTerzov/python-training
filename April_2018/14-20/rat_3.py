rat_1 = [18123, 1321, 3213, 213]
rat_2 = [15223, 423, 32423, 123]

if rat_1[0] > rat_2[0]:
    if rat_1[-1] > rat_2[-1]:
        print("Rat 1  remained heavier than rat 2.")
    else:
        print("Rat 2 became heavier than rat 1.")
else:
    print("Rat 2 became heavier than rat 1.")
    