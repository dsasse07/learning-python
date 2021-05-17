'''
Count the number of times each character appears within a string
'''

def count_chars(str):
  counts = {}
  for ch in str:
    if ch in counts:
      counts[ch] += 1
    else:
      counts[ch] = 1
  return counts

print(count_chars("banana blueberry BAGEL MUFFINS"))