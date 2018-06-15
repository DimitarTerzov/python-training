def find_ditto(list_):
    """ (list) -> set
    
    Find duplicated integer, float or string in list and return result in set.
    
    
    >>> find_ditto([1, 2, 3, 4, 5, 6, 7, 4, 5])
    {4, 5}
    >>> find_ditto(['Green', 'Blue', 'Red', 'Silver', 'Blue'])
    {'Blue'}
    >>> find_ditto([7.1354, 0.01, 5.15, 4.19, 3.1415, 5.15, 0.290213, 0.01,])
    {0.01, 5.15}
    >>> find_ditto([2, 8, 'Jun', 3.14, 7.62, 5.56, 'April', 5, 'November'])
    set()
    """
    
    first_set = set()
    ditto_set = set()
    
    for index in list_:
        len_original = len(first_set)
        value_set.add(index)
        len_duplicate = len(first_set)
        if len_original == len_duplicate:
            ditto_set.add(index)
            
    return(ditto_set)