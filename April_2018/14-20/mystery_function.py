def mystery_function(values):
    """ (list) -> list
    
    Return sublists with reversed values
    
    >>> mystery_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    """
    result = []                         
    for sublist in values:
        # Reverse values in sublists
        result.append([sublist[0]])     
        for i in sublist[1:]:           
            result[-1].insert(0, i)     
    return result
    