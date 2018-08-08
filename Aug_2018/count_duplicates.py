def count_duplicates(d_ry):
    """ (dic) -> int
    
    Return duplicated values in dictionary.
    
    >>> count_duplicates({'AA': 28, 'BB': 35, 'CC': 44, 'DD': 28, 'EE': 35})
    2
    """
    
    duplicates = 0
    values = list(d_ry.values())
    
    for in_nu in values:
        
        # iff an integer_numbers appears at least two times, it is duplicate.
        if values.count(in_nu) >= 2:
            duplicates = duplicates + 1
            
            # extract that integer_number from the list.
            duplicate_occurences = values.count(in_nu)
            for i in range(duplicate_occurences):
                values.remove(in_nu)
                
    return duplicates
