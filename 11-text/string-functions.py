str = "hello friends"
print('str', str)

# Uppercase
print('Uppercase chars of str with .upper()')
print( 'str.upper() ==',str.upper() )
print('str == ', str)

# Lowercase
print('Lowercase chars of str with .lower()')
print( 'str.lower() == ', str.lower() )
print('str == ', str)

# Replace characters
print('Replace all instances of char "l" with "z"')
print('str.replace("l","z") == ', str.replace('l','z'))
print('str.replace("l","") == ', str.replace('l',''))
print('str == ', str)

# Find char in string
print('Find first index of letter in string')
print('If not found, returns -1')
print('str.find("l") == ', str.find('l'))
print('str.find("z") == ', str.find('z'))
print('str == ', str)

# Remove beginning and ending whitespace with .strip
print('Remove leading & trailing whitespace')
spacey = '     hi friend   '
print('spacey ==', spacey)
print('spacey.strip() ==', spacey.strip())

# Split string according to spaces or param
print('Split string according to spaces')
print('str.split() ==', str.split())
print('Split string according to param')
print('str.split("ll") ==', str.split("ll"))

# Starts/Ends With
print('Starts/Ends With')
print('str.startswith("hel") ==', str.startswith("hel"))
print('str.startswith("fa") ==', str.startswith("fa"))
print('str.endswith("ds") ==', str.endswith("ds"))

# Capitalize First Letter with .title()
print('Capitalize First Letter with .title()')
print('str.title() ==', str.title())

# Character classification
print('str.islower()', str.islower())
print('str.isspace()', str.isspace())
print('str.isdigit()', str.isdigit())
