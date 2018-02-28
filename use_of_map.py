kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']for kingdom in map(kingdoms.__getitem__, [0,3]):
    print(kingdom)
print(list(map(kingdoms.__getitem__, [0, 1, 3])))