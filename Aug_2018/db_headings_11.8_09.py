def db_headings(dict_of_dicts):
    """ (dict of dict) -> set
    
    Return a set of the keys in the inner dictionatyes in dect_of_dicts.
    
    >>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2:'c', 3: 'd'}})
    {1, 2, 3}
    >>> db_headings({'rcarson' : {'surname' : 'Carson', 'forename' :
    'Rachel', 'born' : 1907, 'died' : 1964, 'notes' :
    'raised awareness of effects of DDT', 'author' : ['Silent Spring']}})
    {'forename', 'born', 'surname', 'notes', 'author', 'died'}
    """
    
    inner_keys = set()
    
    for key in dict_of_dicts:
        for inner_keys in dict_of_dicts[key]:
            inner_keys.add(inner_keys)
            
    return inner_keys
