""" 2. Python's set objects have a method called pop that removes and returns an
arbitrary element from the set.
"""

def blind_date(females, males):
    """ (set, set) -> set of tuple
    
    Return a set of tuples where each contains a element from females and element from males.
    
    >>> blind_date({'Miss doctor - Anna;33', 'Miss stripper - Jilly;25', 'Miss tennis - Aleks;31
    '}, {'Mr unemployed - Tod;23', 'Mr fisherman - John;29', 'Mr soldier - Jamal;27'})
    >>> {('Miss stripper - Jilly;25', 'Mr fisherman - John;29'), ('Miss doctor - Anna;33', 
    'Mr unemployed - Tod;23'), ('Miss tennis - Aleks;31', 'Mr soldier - Jamal;27')}
    """
    
    pairs = set()
    num_bride = len(females)
    
    for breast in range(num_bride):
        
        female = females.pop()
        male = males.pop()
        pairs.add((female,male),)
        
    return pairs
