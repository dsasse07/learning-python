import random

NUM_SIDES = 6

def main():
  die1 = 10
  print('die1 in main() starts as:',die1)
  roll_dice()
  roll_dice()
  roll_dice()
  print('die1 in main() endss as:',die1)


def roll_dice():
  die1 = random.randint(1,NUM_SIDES)
  die2 = random.randint(1,NUM_SIDES)
  total = die1 + die2
  print('Rolling Dice...')
  print('You rolled a', die1, 'and',die2)
  print('For a total of', total)

main()