for line in open('1lgd.pdb'):
    if line.startswith('AUTHOR'):
        print(line)
        