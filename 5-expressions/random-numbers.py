import random

'''
random.randint(min, max) #random INTEGER inclusive
random.random() # Random FLOAT between 0 and 1
random.uniform(min, max) # Random FLOAT between min and max
random.seed(x)  # Sets seed of generator to X
'''

NUM_SIDES = 6

def main():
  die1 = random.randint(1,NUM_SIDES)
  die2 = random.randint(1,NUM_SIDES)
  total = die1 + die2

  print('Dice have', NUM_SIDES, 'sides each.')
  print('First die:', die1)
  print('Second die:', die2)
  print('Total of two dice:', total)

main()