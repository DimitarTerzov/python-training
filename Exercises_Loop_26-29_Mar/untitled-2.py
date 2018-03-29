week = 1
while rat_1_weight[week] / rat_1_weight[0] - 1 < .25:
    week += 1
print(week)
