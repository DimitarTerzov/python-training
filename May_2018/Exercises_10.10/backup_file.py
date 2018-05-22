filename = input('Write filename and extension to BACKUP: ')
    # Run file on Wing 5.1 to know where is the backup file location,
    # Hint: hebron.txt this file contents will be copied,
    # and new file hebron.txt.bak will be created in same folder,
    # new file can be open with Wing 5.1
new_filename = filename + '.bak'
backup = open(new_filename, 'w')

for line in open(filename):
    backup.write(line)
    
backup.close()

import os
print(os.path.abspath(new_filename))
os.system('explorer')
os.startfile(new_filename)
