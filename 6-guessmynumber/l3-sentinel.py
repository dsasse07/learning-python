def main():
  print('This program will add all of the numbers you enter until you type a negative value.')
  number = int(input('Enter a number :'))
  total = 0

  while number >= 0:
    total += number
    print('The current total is %i'%(total)) 
    print('') 
    number = int(input('Enter another number :'))

main()
