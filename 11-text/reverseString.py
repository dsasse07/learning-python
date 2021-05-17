
def reverse_str(str):
  reverse = ''
  for char in str:
    reverse = char + reverse
  return reverse

print(reverse_str('hello'))