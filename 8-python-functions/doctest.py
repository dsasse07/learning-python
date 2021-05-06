'''
to run doctest:

python -m doctest filename.py
'''


def main():
  return factorial(5)

def factorial(num):
  '''
  Calculate n factorial
  5! = 5 * 4 * 3 * 2 * 1
  >>> factorial(5)
  120
  >>> factorial(4)
  24
  >>> factorial(3)
  6
  >>> factorial(2)
  2
  >>> factorial(1)
  1
  '''
  if num == 1 or num == 0:
    return num
  value = num * factorial(num-1)
  return value

print(main())