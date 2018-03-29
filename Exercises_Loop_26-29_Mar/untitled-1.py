rat_1 = [105, 110, 120, 125, 130, 135, 140, 145, 150, 160]
rat_2 = [120, 127, 133, 144, 151, 160, 166, 171, 180, 188]
if rat_1[0] > rat_2[0]:
    if rat_1[-1] > rat_2[-1]:
        print("Rat 1 remainded heavier than Rat 2.")
    else:
        print("Rat 2 became heavier than Rat 1.")
else:
    print("Rat 2 became heavier than Rat 1.")
    
    