def get_authors(filemanes):
    """ (list of str) -> set of str
    
    Return a list of the authors in PDB files names appear in filenames.
    """
    
    authors = set()
    
    for filename in filenames:
        pdb_file = open(filename)
        
        for line in pdb_file:
            if line.lower().startswith('author'):
                author = line[6:].strip()
                authors.add(author)
                
    return authors
