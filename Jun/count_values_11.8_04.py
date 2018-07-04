def count_values(dictionary):
    """ (dict) -> int
    
    Return the number of unique values in dictionary.
    
    >>> count_values({'humans': 5, 'planets': 8, 'balls: 5'})
    2
    """
    return len(set(dictionary.values()))
