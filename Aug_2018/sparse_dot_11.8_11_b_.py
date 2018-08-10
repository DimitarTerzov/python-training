def sparse_dot(vector1, vector2):
    """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})
    
    Return the dot product of sparse vectors vector1 and vector2.
    
    >>> sparse_dot({3:5, 5:5}, {2:4, 3:5, 5:10})
    75
    """
    
    dot = 0
    
    for key1 in vector1:
        if key1 in vector2:
            dot = dot + vector1[key1] * vector2[key1]
            
    return dot
