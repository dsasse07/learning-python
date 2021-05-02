import random

def main():
  number = random.randint(1,99)
  print('Welcome to Guess My Number!')
  print('I am thinking of a number betwee 1 and 99.')
  print('What do you think it is?')
  guess = int(input('Enter a guess: '))
  while not guess == number:
    outcome = 'low' if guess < number else 'high'
    print('Your guess is too ' + outcome + '. Try again!')
    guess = int(input('Enter a guess: '))
  print('You guessed correctly! The number was %i'%(number))

main()

