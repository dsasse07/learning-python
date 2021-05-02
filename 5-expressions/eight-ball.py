
import random

ANSWERS = [
  'Definitely Not',
  'For sure!',
  'Absolutely',
  'The answer is unclear',
  'Try again later'
]
def main():
  print('Welcome to the magic 8 ball.')
  question = input('Ask a yes or no question, or type "no" to exit:')
  while question != "no":
    print( ANSWERS[random.randint(1, len(ANSWERS) )])
    question = input('Ask a yes or no question, or type "no" to exit:')


main()