def db_consistent(dict_of_dicts):
    """ (dict of dict) -> set
    
    Return whether all inner dictionaryes in dict_of_dicts
    contain the same keys.
    
    >>> db_consistent({'LIST_15': {'code': 345, 'name': 'John'}, 'LIST_20':
    {'code': 678, 'country': 'San Marino'}})
    False
     
    >>> db_consistent({'LIST_460': {'human': 'J.T.P.', 'born': 1971}, 'LIST_810': 
    {'born': 1944, 'human': 'W.R.K.'}})
    True
    """
    
    inner_keys_list = []
    
    # Build a list of list of keys.
    for key in dict_of_dicts:
        inner_keys = list(dict_of_dicts[key].keys())
        inner_keys.sort()
        inner_keys_list.append(inner_keys)
        
    for i in range(1, len(inner_keys_list)):
        
        # Iff the number of keys is different.
        if len(inner_keys_list[0]) != len(inner_keys_list[1]):
            return False
        
        # Iff the keys don't match.
        for j in range(len(inner_keys_list[0])):
            if inner_keys_list[0][j] != inner_keys_list[i][j]:
                return False
            
    return True
            