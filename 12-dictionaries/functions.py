# Dictionary Examples
ages = {'Danny':32, 'Nicole':31}
squares = {2: 4,3: 9, 4: 16}
empty = {}

# Access Elements
print(ages['Danny'])

# Set Elements
ages['Mehran'] = 53

# Key in dict??
print( 'Kevin' in ages) #False
print( 'Kevin' not in ages) #True

phone = {}
phone['Pat'] = '555-1212'
phone['Jenny'] = '867-5309'

#Erase value of a key without deleting key
phone['Pat'] = None

'''
  Dictionay Functions
'''
# Key lookup WITHOUT ERROR
print('phone.get("Danny")', phone.get('Danny')) # Null
print("phone.get('Jenny')", phone.get('Jenny')) # 867-5309
# Can also pass a second param to .get() to use as default
print('2nd .dict() param will be used as default')
print('phone.get("Danny", "No Number")', phone.get('Danny', "No Number")) # No Number

# Get all keys of a dict
print("ages.keys()", ages.keys())
print('.keys() return a list-like result that is iterable, but is not a list')
print('result can be cast into a list by doing list(dict.keys())')

# Get all values of a dict
print(ages.values())
print('.values() return a list-like result that is iterable, but is not a list')
print('result can be cast into a list by doing list(dict.values())')

# Remove a key:value pair from a dictionary with .pop(key).
# Returns VALUE of that pair
print('ages',ages)
print("ages.pop('Mehran')", ages.pop('Mehran'))
print('ages',ages)

# Remove all pairs with dict.clear()
# ages.clear == {}

# Functions you can apply
print('How many k:v pairs? Use len()')
print('len(ages)', len(ages))

print('Delete a pair with no return')
print('ages',ages)
print('del ages["Danny"]')
del ages["Danny"]
print('ages',ages)