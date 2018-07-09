def least_likely(particle_to_probability):
    
    positions = []              # output variable
    min_value = float("inf")
    
    for key, value in particle_to_probability.items():
        if value == min_value:
            positions.append(key)
        if value < min_value:
            min_value = value
            positions = []      # output variable
            positions.append(key)
    """ 
    least_likely({'a':0.351, 'b':0.015, 'c':0.099, 'd':0.224, 'e':0.015})

    ['e', 'b']
    """
            
    return positions
