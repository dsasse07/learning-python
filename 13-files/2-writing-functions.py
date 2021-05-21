import os
dirname = os.path.dirname(__file__)

def file(r_path):
  return os.path.join(dirname, r_path)

# Gives write access to the file
# If filename exists, it will be erased and re-written
# If filename does not exist, it will be created
names = ['Frodo', 'Eowyn', 'Treebeard']
with open(file('test_write.txt'),'w') as first_file:
  first_file.write('longing\n')
  first_file.write('two lines\n')
  first_file.writelines(names)


