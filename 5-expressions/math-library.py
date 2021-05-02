import math
"""
math.pi
math.e
math.sqrt
math.exp => e ^ x
math.log => log_e (x)
"""
print(math.pi)

def main():
  print("This program returns the square root of a num")
  num = float( input('Enter a number:'))
  root = math.sqrt(num)
  print('The square root of', num, 'is', root)

main()