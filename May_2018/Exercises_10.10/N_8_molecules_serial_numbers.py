def read_molecule(reader):
    """ (file open for reading) -> list or NoneType
    
    Read one molecule and return it, or return None for file end.
    The first item is the element name, each list contains an atom type
    and the X, Y, and Z co-ordinates of that atom.
    """
    
    # If there isn't another line, we're at the end of the file,
    # and return None.
    line = reader.readline()
    if not line:
        return None
    
    # Name of the molecule: "Compound, Name"
    key, name = line.split()
    
    # Other lines are either "END" or "ATOM, num, atom_type, x, y, z"
    
    molecule = [name]
    reading = True
    
    serial_number = 1
    
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, atom_type, x, y, z = line.split()
            if int(num) != serial_number:
                print("Expected serial number {0}, and we got {1}".format(
                    serial_number, num))
                # So stupid task.
                molecule.append([atom_type, x, y, z])
                serial_number += 1
    return molecule

def read_all_molecules(reader):
    """ (file open for reading) -> list
    
    Read all molecules from reader, returning a list of the molecules info.
    """
    
    # The list of molecules info.
    result = []
    
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:        
            # None is treated as False in an if statement.
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('multimolecules_file_003.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
  