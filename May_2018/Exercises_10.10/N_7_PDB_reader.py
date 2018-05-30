def read_molecule(reader):
    """ (file open for read) -> list or NoneType
    
    Read a single molecule from reader and return it, or return None
    to signal the end of file. The first item in the result is the name
    of the compound; each list contains an atom type and the X, Y, and Z 
    coordinates of that atom.
    """
    
    # If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None
    
    if not (line.startswith('CMNT') or line.isspace()):
        # Name of the molecule: "COMPND ******"
        key, name = line.split()
        
        # Other lines are either "AND" or "ATOM num atom_type x y z"
        molecule = [name]
    else:
        molecule = None
        
    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        elif not (line.startswith('CMNT') or line.isspace()):
            # Function for CMNT and a blank line work only between line COMPND and END
            # for each element, NOT between the elements
            key, num, atom_type, x, y, z = line.split()
            if molecule == None:
                molecule = []
            molecule.append([atom_type, x, y, z])
            
    return molecule

def read_all_molecules(reader):
    """ (file open for reading) -> list
    
    Read molecules from reader, returning a list of the molecule info.
    """
    
    # The list of molecule info.
    result = []
    
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:        # None is treated as False in an if statement.
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('multimolecules_file.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    print(molecules)
    