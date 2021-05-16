'''
Write a program in the file subtract_numbers.py that reads two real numbers from the user and prints the first number minus the second number.

$ python subtract_numbers.py
This program subtracts one number from another.
Enter first number: 5.5
Enter second number: 2.1
The result is 3.4
'''

def main():
  print('This program subtracts one number from another.')
  num1 = float(input('Enter first number: '))
  num2 = float(input('Enter second number: '))
  answer = round( num1 - num2, 1)
  print('The result is ' + str(answer))

main()