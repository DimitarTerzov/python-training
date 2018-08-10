def sparse_add(vector1, vector2):
    """ 9dict of {int: int}, dict of {int: int} -> dict of {int: int})
    
    Return the sum of sparse vectors vector1 and vector2.
    
    >>> sparse_add({1:21, 2:25, 3:55, 6:80}, {1:9, 2:5, 3:45, 4:44, 5:55, 6:100})
    {1: 30, 2: 30, 3: 100, 4: 44, 5: 55, 6: 180}
    """
    
    sum_vector = vector1.copy()
    
    for key in vector2:
        if key in sum_vector:
            sum_vector[key] = sum_vector[key] + vector2[key]
        else:
            sum_vector[key] = vector2[key]
            
    return sum_vector
