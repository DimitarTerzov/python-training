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
            key_of_dict = " ".join(positions)
            """ Line 13 remove brackets and iff function is without this
            line, the Return work with two equally values and return
            two keys in dictionary. Now return only one key in string.
            
            least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07})
            
            'meson'
            """
            
    return key_of_dict
