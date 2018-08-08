def is_balanced(color_to_factor):
    """ (dict of {str: float}) -> bool
    
    Return True iff and only iff color_to_factor represents a balaced color.
    Balanced color is R + G + B == 1.0
    
    >>> is_balanced({'R': 0.5, 'G': 0.6, 'B': 0.9})
    False
    >>> is_balanced({'R': 0.1, 'G': 0.2, 'B': 0.3})
    True
    """
    
    values = list(color_to_factor.values())
    total = sum(values)
    return total == 1.0
    