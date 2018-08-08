def dict_intersect(dict1, dict2):
    """ (dict, dict) -> dict
    
    Return a new dictionary with contains only the pairs key//values
    that occur in both dict1 and dict2.
    
    >>> dict_intersect({'R': 0.5, 'G': 0.6, 'B': 0.9}, {'R': 0.1, 'G': 0.6, 'B': 0.1})
    {'G': 0.6}
    """
    
    duplicate_key_value = {}
    
    for (key, value) in dict1.items():
        if key in dict2 and value == dict2[key]:
            duplicate_key_value[key] = value
            
    return duplicate_key_value
