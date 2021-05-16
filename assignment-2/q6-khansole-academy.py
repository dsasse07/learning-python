import random
'''
Prints out a randomly generated addition problem
and checks if the user answers correctly.
'''

def main():
  num1 = random.randint(10,99)
  num2 = random.randint(10,99)
  answer = num1 + num2
  print('What is ' + str(num1) + ' + ' + str(num2) + '?')
  guess = int(input('Your answer: '))
  if guess == answer:
    print('Correct!')
  else:
    print('Incorrect. The expected answer is ' + str(answer))

main()