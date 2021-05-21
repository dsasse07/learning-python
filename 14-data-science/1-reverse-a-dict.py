ages = {
  'Mehran':51,
  'Gary':70,
  'Chris':33,
  'Freya':1,
  'Adele':33,
  'Lionel':33,
  'Rihanna':33,
  'Stephen':33
}

def reverse(dict):
  reverse = {}

  for name, age in dict.items():
    if age in reverse: reverse[age].append(name)
    else: reverse[age] = [name]
  
  return reverse
  


print(reverse(ages))

