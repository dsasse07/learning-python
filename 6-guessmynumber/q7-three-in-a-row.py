import random

'''
This will generate 2-digit addition problems until the user
gets 3 in a row correct.
'''

REQUIRED_STREAK = 3

def main():
  print('Welcome to Khansole Academy.')
  print("Let's practice addition until you get " + str(REQUIRED_STREAK) + " in a row correct")
  streak = 0

  while streak < REQUIRED_STREAK:
    if ask_question():
      streak += 1
      print("Correct! You've gotten " + str(streak) + " correct in a  row.")
    else:
      streak = 0
  print('Congratulations! You mastered addition.')


def ask_question():
  num1 = random.randint(10,99)
  num2 = random.randint(10,99)
  answer = num1 + num2
  print('What is ' + str(num1) + ' + ' + str(num2) + '?')
  guess = int(input('Your answer: '))
  if guess != answer:
    print('Incorrect. The expected answer is ' + str(answer))
  return guess == answer

main()