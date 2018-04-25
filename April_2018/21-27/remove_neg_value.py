def remove_neg(num_list):
    """ (list of numbers) -> NoneType
    
    Remove the negative numbers from the list num_list.
    
    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    """
    
    index = 0
    while index < len(num_list):
        if num_list[index] < 0:
            del num_list[index]
        else:
            index += 1
            
            