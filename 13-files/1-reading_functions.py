import os
dirname = os.path.dirname(__file__)

def file(r_path):
  return os.path.join(dirname, r_path)
'''
  By default Python is looking for absolute path.
  Use the above to generate abs path from relative path
'''

# Open a file
this_file = open(file('invictus.txt'))

for line in this_file: 
  print(line.rstrip()) # or .strip('/n') or .lstrip()

# Close file
this_file.close()

# Using the with keyword to open files creates the file
# and automatically closes it
print('***************************')

with open(file('invictus.txt')) as second_file:
  for line in second_file:
      print(line.rstrip()) # or .strip('/n') or .lstrip()

print('***************************')

# Skipping a line in a file (or any pass through loop)
third_file = open(file('invictus.txt'))
next(third_file)
for line in third_file: 
  print(line.rstrip()) # or .strip('/n') or .lstrip()
third_file.close()

print('***************************')
# Store contents of text file in variable
with open(file('invictus.txt')) as fourth_file:
  lines = fourth_file.readlines()
  print(lines)
