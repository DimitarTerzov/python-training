with open('alkaline_metals.txt', 'r') as elements_file:
    elements = elements_file.readlines()
    
    elements = [x.strip() for x in elements]

    

    print([[i] for i in elements])